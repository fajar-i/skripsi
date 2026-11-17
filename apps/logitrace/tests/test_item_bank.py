"""
Unit Tests for L2 Item Bank: 180 Adaptive Items, 10 Parallel TOLT, and 6 NEDV Controls.
Includes happy path validation and negative / edge-case validation suites.
"""

import copy
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data.l2_item_bank.schema_validator import (
    validate_adaptive_bank,
    validate_troubleshooting_parallel_test,
    validate_nedv_controls,
    _safe_load_json
)


class TestItemBankIntegrity(unittest.TestCase):
    """Happy path validation tests on production JSON item banks."""

    def test_adaptive_180_items_balance(self):
        """180 items must be distributed across 12 KCs (5 easy, 5 med, 5 hard each) with balanced keys."""
        ok, errors = validate_adaptive_bank()
        self.assertTrue(ok, f"Adaptive bank validation failed: {errors}")

    def test_troubleshooting_parallel_forms(self):
        """Parallel Cognitive Troubleshooting Form A and Form B must each contain 36 items (30 target + 6 NEDV)."""
        ok, errors = validate_troubleshooting_parallel_test()
        self.assertTrue(ok, f"Troubleshooting parallel test validation failed: {errors}")

    def test_nedv_control_integrity(self):
        """6 NEDV control items must consist of 2 VoIP items and 4 Fiber Optic items."""
        ok, errors = validate_nedv_controls()
        self.assertTrue(ok, f"NEDV control items validation failed: {errors}")


class TestItemBankNegativeEdgeCases(unittest.TestCase):
    """Negative unit tests verifying that validators catch structural, psychometric, and syntax flaws."""

    def setUp(self):
        # Load sample valid bank data
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "l2_item_bank"))
        items_path = os.path.join(base_dir, "items_adaptive_180.json")
        with open(items_path, "r", encoding="utf-8") as f:
            self.valid_items = json.load(f)

    def _write_temp_json(self, data) -> str:
        tmp = tempfile.NamedTemporaryFile("w", delete=False, suffix=".json", encoding="utf-8")
        json.dump(data, tmp)
        tmp.close()
        return tmp.name

    def test_catches_duplicate_item_id(self):
        """Validator must fail when duplicate item IDs exist."""
        bad_items = copy.deepcopy(self.valid_items)
        bad_items[1]["id"] = bad_items[0]["id"]  # Duplicate ID
        path = self._write_temp_json(bad_items)
        try:
            ok, errors = validate_adaptive_bank(path)
            self.assertFalse(ok)
            self.assertTrue(any("Duplicate item ID" in err for err in errors))
        finally:
            os.remove(path)

    def test_catches_skewed_answer_distribution(self):
        """Validator must fail when answer key distribution is severely skewed (> 32% or < 18%)."""
        bad_items = copy.deepcopy(self.valid_items)
        # Force 80% of answers to be "A"
        for item in bad_items[:150]:
            item["correct_answer"] = "A"
        path = self._write_temp_json(bad_items)
        try:
            ok, errors = validate_adaptive_bank(path)
            self.assertFalse(ok)
            self.assertTrue(any("skewed" in err.lower() for err in errors))
        finally:
            os.remove(path)

    def test_catches_non_root_calibration_item(self):
        """Validator must reject calibration items placed on non-root KCs."""
        bad_items = copy.deepcopy(self.valid_items)
        # Find item on non-root KC like ICMP_CONNECTIVITY and mark as calibration
        for item in bad_items:
            if item["primary_kc"] == "ICMP_CONNECTIVITY":
                item["is_calibration"] = True
                break
        path = self._write_temp_json(bad_items)
        try:
            ok, errors = validate_adaptive_bank(path)
            self.assertFalse(ok)
            self.assertTrue(any("non-root" in err.lower() for err in errors))
        finally:
            os.remove(path)

    def test_catches_missing_prompt_or_answer(self):
        """Validator must fail if prompt is blank or answer is not in options."""
        bad_items = copy.deepcopy(self.valid_items)
        bad_items[0]["prompt_text"] = "   "  # Empty whitespace
        bad_items[1]["correct_answer"] = "Z"  # Missing option
        path = self._write_temp_json(bad_items)
        try:
            ok, errors = validate_adaptive_bank(path)
            self.assertFalse(ok)
            self.assertTrue(any("Empty prompt" in err for err in errors))
            self.assertTrue(any("not found in options" in err for err in errors))
        finally:
            os.remove(path)

    def test_safe_load_catches_malformed_json(self):
        """_safe_load_json must handle malformed JSON syntax without throwing unhandled exceptions."""
        tmp = tempfile.NamedTemporaryFile("w", delete=False, suffix=".json", encoding="utf-8")
        tmp.write("{ invalid json content: [ ]")
        tmp.close()
        try:
            ok, data, err_msg = _safe_load_json(tmp.name)
            self.assertFalse(ok)
            self.assertIn("Malformed JSON", err_msg)
        finally:
            os.remove(tmp.name)


if __name__ == "__main__":
    unittest.main(verbosity=2)


def test_no_static_hint_leaks_any_item_answer():
    """Every static hint must pass the leakage guard for every item of its KC."""
    import json as _json
    from backend.app.rag.guardrails import AnswerLeakageGuard

    base = os.path.join(os.path.dirname(__file__), "..", "data")
    with open(os.path.join(base, "fallback_hints", "static_hints.json"), encoding="utf-8") as f:
        hints = _json.load(f)
    with open(os.path.join(base, "l2_item_bank", "items_adaptive_180.json"), encoding="utf-8") as f:
        items = _json.load(f)
    guard = AnswerLeakageGuard()
    leaks = [
        (it["id"], lvl)
        for it in items
        for lvl, text in hints[it["primary_kc"]].items()
        if not guard.check_leakage(text, it["options"][it["correct_answer"]], list(it["options"].values()))[0]
    ]
    assert leaks == []


def test_dag_sources_agree():
    """dag_prerequisites.json (runtime) and kcs.json must describe the same graph."""
    import json as _json

    base = os.path.join(os.path.dirname(__file__), "..", "data", "l1_knowledge_base")
    with open(os.path.join(base, "dag_prerequisites.json"), encoding="utf-8") as f:
        dag = _json.load(f)
    with open(os.path.join(base, "kcs.json"), encoding="utf-8") as f:
        kcs = _json.load(f)
    from_edges = {}
    for e in dag["edges"]:
        from_edges.setdefault(e["to"], set()).add(e["from"])
    for kc in kcs:
        assert set(kc["prerequisites"]) == from_edges.get(kc["id"], set()), kc["id"]
        assert kc["is_root"] == (kc["id"] in dag["roots"])
        assert dag["in_degrees"][kc["id"]] == len(from_edges.get(kc["id"], set()))
