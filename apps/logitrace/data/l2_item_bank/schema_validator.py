"""
LogiTrace: Bank Soal L2 Schema Validator & Audit Suite.
Validates structural integrity, distribution balance, psychometric answer key distribution,
ID uniqueness, and curriculum coverage of L2 bank.
"""

import collections
import json
import logging
import os
import sys
from typing import Dict, List, Set, Tuple

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("schema_validator")

BASE_DIR = os.path.dirname(__file__)
ITEMS_PATH = os.path.join(BASE_DIR, "items_adaptive_180.json")
TOLT_PATH = os.path.join(BASE_DIR, "tolt_test_parallel.json")
TROUBLESHOOTING_PATH = os.path.join(BASE_DIR, "troubleshooting_test_parallel.json")
NEDV_PATH = os.path.join(BASE_DIR, "nedv_control_items.json")

EXPECTED_KCS = {
    "WLAN_STANDARDS", "WLAN_TOPOLOGY_BSS", "IP_PEER_CONFIG",
    "WLAN_FREQ_CHANNEL", "WLAN_SECURITY_AUTH", "WLAN_HOST_HARDENING",
    "WLAN_SIGNAL_PROP", "WLAN_ROAMING_PROB", "WLAN_CHANNEL_COLLISION",
    "ICMP_CONNECTIVITY", "ICMP_TROUBLE_DHU", "ICMP_TROUBLE_RTO"
}

EXPECTED_TOLT_DIMS = {
    "CONTROLLING_VARIABLES",
    "PROPORTIONAL_REASONING",
    "COMBINATORIAL_REASONING",
    "PROBABILISTIC_REASONING",
    "CORRELATIONAL_REASONING"
}

EXPECTED_JONASSEN_PHASES = {
    "SYMPTOM_RECOGNITION",
    "PROBLEM_SPACE_CONSTRUCTION",
    "FAULT_HYPOTHESIS_GENERATION",
    "HYPOTHESIS_TESTING_EVALUATION",
    "CORRECTIVE_ACTION_VERIFICATION"
}

ROOT_KCS = {"WLAN_STANDARDS", "WLAN_TOPOLOGY_BSS", "IP_PEER_CONFIG"}


def _safe_load_json(file_path: str) -> Tuple[bool, any, str]:
    """Safely loads JSON with file existence and decode exception handling."""
    if not os.path.exists(file_path):
        return False, None, f"File does not exist: {file_path}"
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return True, data, ""
    except json.JSONDecodeError as err:
        return False, None, f"Malformed JSON in {file_path}: {err}"
    except OSError as err:
        return False, None, f"I/O error reading {file_path}: {err}"


def validate_adaptive_bank(file_path: str = ITEMS_PATH) -> Tuple[bool, List[str]]:
    """
    Validates the 180-item adaptive question bank:
    - Exactly 180 items
    - Unique item IDs
    - 12 KCs with 15 items each (5 easy, 5 med, 5 hard)
    - 6 calibration items across root KCs (2 easy, 2 med, 2 hard)
    - Balanced answer key distribution across {"A", "B", "C", "D"} (18% - 32%)
    """
    errors: List[str] = []
    success, items, err_msg = _safe_load_json(file_path)
    if not success:
        return False, [err_msg]

    if not isinstance(items, list):
        return False, ["Adaptive bank root must be a list of items"]

    if len(items) != 180:
        errors.append(f"Expected 180 items, got {len(items)}")

    seen_ids: Set[str] = set()
    kc_counts: Dict[str, Dict[int, int]] = {kc: {1: 0, 2: 0, 3: 0} for kc in EXPECTED_KCS}
    calibration_count = 0
    calibration_diffs = {1: 0, 2: 0, 3: 0}
    answer_keys: List[str] = []

    for idx, item in enumerate(items):
        item_id = item.get("id", f"idx_{idx}")

        # ID uniqueness
        if item_id in seen_ids:
            errors.append(f"Duplicate item ID detected: '{item_id}'")
        seen_ids.add(item_id)

        kc = item.get("primary_kc")
        diff = item.get("difficulty")
        tolt = item.get("tolt_dimension")
        opts = item.get("options", {})
        ans = item.get("correct_answer")

        # Field validations
        if kc not in EXPECTED_KCS:
            errors.append(f"{item_id}: Unknown or missing KC '{kc}'")
        if diff not in (1, 2, 3):
            errors.append(f"{item_id}: Invalid difficulty '{diff}'")
        if tolt not in EXPECTED_TOLT_DIMS:
            errors.append(f"{item_id}: Invalid TOLT dimension '{tolt}'")
        if not item.get("prompt_text") or not str(item.get("prompt_text")).strip():
            errors.append(f"{item_id}: Empty prompt text")
        if not isinstance(opts, dict) or len(opts) < 4:
            errors.append(f"{item_id}: Options must have at least 4 choices (A, B, C, D)")
        if ans not in opts:
            errors.append(f"{item_id}: Correct answer '{ans}' not found in options")
        else:
            answer_keys.append(ans)

        if kc in kc_counts and diff in (1, 2, 3):
            kc_counts[kc][diff] += 1

        if item.get("is_calibration"):
            calibration_count += 1
            if diff in calibration_diffs:
                calibration_diffs[diff] += 1
            if kc not in ROOT_KCS:
                errors.append(f"{item_id}: Calibration item belongs to non-root KC '{kc}'")

    # Verify 15 items per KC (5 easy, 5 med, 5 hard)
    for kc, diff_map in kc_counts.items():
        for d in (1, 2, 3):
            count = diff_map[d]
            if count != 5:
                errors.append(f"KC {kc} difficulty {d} expected 5 items, got {count}")

    # Verify calibration distribution
    if calibration_count != 6:
        errors.append(f"Expected 6 calibration items, got {calibration_count}")
    for d in (1, 2, 3):
        if calibration_diffs[d] != 2:
            errors.append(f"Calibration difficulty {d} expected 2 items, got {calibration_diffs[d]}")

    # Verify answer key distribution balance (18% - 32% per option)
    if answer_keys:
        key_counts = collections.Counter(answer_keys)
        total_answers = len(answer_keys)
        for opt in ("A", "B", "C", "D"):
            ratio = key_counts[opt] / total_answers
            if not (0.18 <= ratio <= 0.32):
                errors.append(
                    f"Option '{opt}' key ratio skewed: {ratio:.1%} ({key_counts[opt]}/{total_answers}), expected ~25%"
                )

    return len(errors) == 0, errors


def validate_tolt_parallel_test(file_path: str = TOLT_PATH) -> Tuple[bool, List[str]]:
    """
    Validates parallel TOLT instruments (Form A and Form B):
    - Exactly 10 items in Form A and 10 items in Form B
    - Unique item IDs
    - 2 items per TOLT dimension (all 5 dimensions represented)
    - Non-empty prompt, options == 4, correct_option in options
    - Reasoning options >= 3, correct_reasoning in reasoning_options
    - Balanced answer key distribution across forms
    """
    errors: List[str] = []
    success, data, err_msg = _safe_load_json(file_path)
    if not success:
        return False, [err_msg]

    if not isinstance(data, dict):
        return False, ["TOLT file root must be a JSON object with 'form_a' and 'form_b'"]

    seen_ids: Set[str] = set()

    for form_name in ("form_a", "form_b"):
        items = data.get(form_name, [])
        if not isinstance(items, list) or len(items) != 10:
            errors.append(f"{form_name}: Expected 10 items, got {len(items) if isinstance(items, list) else 0}")
            continue

        dim_counts = {dim: 0 for dim in EXPECTED_TOLT_DIMS}
        form_keys: List[str] = []

        for item in items:
            item_id = item.get("id", "UNKNOWN")
            if item_id in seen_ids:
                errors.append(f"Duplicate TOLT item ID: '{item_id}'")
            seen_ids.add(item_id)

            dim = item.get("dimension")
            if dim in dim_counts:
                dim_counts[dim] += 1
            else:
                errors.append(f"{item_id}: Unknown dimension '{dim}'")

            prompt = item.get("prompt")
            if not prompt or not str(prompt).strip():
                errors.append(f"{item_id}: Empty prompt text")

            opts = item.get("options", {})
            if not isinstance(opts, dict) or len(opts) != 4:
                errors.append(f"{item_id}: Expected exactly 4 options (A, B, C, D), got {len(opts)}")

            ans = item.get("correct_option")
            if ans not in opts:
                errors.append(f"{item_id}: correct_option '{ans}' not found in options")
            else:
                form_keys.append(ans)

            # Polytomous reasoning options check
            r_opts = item.get("reasoning_options", {})
            if not isinstance(r_opts, dict) or len(r_opts) < 3:
                errors.append(f"{item_id}: Expected at least 3 reasoning options for polytomous scoring")

            r_ans = item.get("correct_reasoning")
            if r_ans not in r_opts:
                errors.append(f"{item_id}: correct_reasoning '{r_ans}' not found in reasoning_options")

        # Each dimension must have exactly 2 items
        for dim, cnt in dim_counts.items():
            if cnt != 2:
                errors.append(f"{form_name} dimension {dim} expected 2 items, got {cnt}")

        # Form answer key balance: no single option should exceed 50%
        key_counts = collections.Counter(form_keys)
        for opt, cnt in key_counts.items():
            if cnt > 5:
                errors.append(f"{form_name}: Option '{opt}' overrepresented ({cnt}/10)")

    return len(errors) == 0, errors


def validate_troubleshooting_parallel_test(file_path: str = TROUBLESHOOTING_PATH) -> Tuple[bool, List[str]]:
    """
    Validates parallel Cognitive Troubleshooting instruments (Form A and Form B)
    based on David H. Jonassen & Woei Hung (2006):
    - Exactly 36 items in Form A and 36 items in Form B
    - Unique item IDs across both forms
    - Exactly 6 items per Jonassen phase (5 phases x 6 = 30 target items)
    - Exactly 6 NEDV control items (2 VoIP + 4 Fiber Optic)
    - Non-empty prompt, options == 4, correct_option in options
    - Reasoning options >= 3, correct_reasoning in reasoning_options
    - Balanced answer key distribution across forms
    """
    errors: List[str] = []
    success, data, err_msg = _safe_load_json(file_path)
    if not success:
        return False, [err_msg]

    if not isinstance(data, dict):
        return False, ["Troubleshooting file root must be a JSON object with 'form_a' and 'form_b'"]

    seen_ids: Set[str] = set()

    for form_name in ("form_a", "form_b"):
        items = data.get(form_name, [])
        if not isinstance(items, list) or len(items) != 36:
            errors.append(f"{form_name}: Expected 36 items, got {len(items) if isinstance(items, list) else 0}")
            continue

        phase_counts = {phase: 0 for phase in EXPECTED_JONASSEN_PHASES}
        phase_counts["NEDV_CONTROL"] = 0
        form_keys: List[str] = []

        for item in items:
            item_id = item.get("id", "UNKNOWN")
            if item_id in seen_ids:
                errors.append(f"Duplicate troubleshooting item ID: '{item_id}'")
            seen_ids.add(item_id)

            phase = item.get("phase")
            if phase in phase_counts:
                phase_counts[phase] += 1
            else:
                errors.append(f"{item_id}: Unknown troubleshooting phase '{phase}'")

            prompt = item.get("prompt")
            if not prompt or not str(prompt).strip():
                errors.append(f"{item_id}: Empty prompt text")

            opts = item.get("options", {})
            if not isinstance(opts, dict) or len(opts) != 4:
                errors.append(f"{item_id}: Expected exactly 4 options (A, B, C, D), got {len(opts)}")

            ans = item.get("correct_option")
            if ans not in opts:
                errors.append(f"{item_id}: correct_option '{ans}' not found in options")
            else:
                form_keys.append(ans)

            # Polytomous reasoning options check
            r_opts = item.get("reasoning_options", {})
            if not isinstance(r_opts, dict) or len(r_opts) < 3:
                errors.append(f"{item_id}: Expected at least 3 reasoning options for polytomous scoring")

            r_ans = item.get("correct_reasoning")
            if r_ans not in r_opts:
                errors.append(f"{item_id}: correct_reasoning '{r_ans}' not found in reasoning_options")

        # Each target phase must have exactly 6 items
        for phase in EXPECTED_JONASSEN_PHASES:
            cnt = phase_counts[phase]
            if cnt != 6:
                errors.append(f"{form_name} phase {phase} expected 6 items, got {cnt}")

        # NEDV control must have exactly 6 items
        if phase_counts["NEDV_CONTROL"] != 6:
            errors.append(f"{form_name} NEDV_CONTROL expected 6 items, got {phase_counts['NEDV_CONTROL']}")

        # Form answer key balance: no single option should exceed 40% (15 out of 36)
        key_counts = collections.Counter(form_keys)
        for opt, cnt in key_counts.items():
            if cnt > 15:
                errors.append(f"{form_name}: Option '{opt}' overrepresented ({cnt}/36)")

    return len(errors) == 0, errors


def validate_nedv_controls(file_path: str = NEDV_PATH) -> Tuple[bool, List[str]]:
    """
    Validates NEDV control items (Threat to Internal Validity C2):
    - Exactly 6 items
    - Unique item IDs
    - Exactly 2 VoIP items (TP 2.3) and 4 Fiber Optik items (TP 2.4/2.5)
    - Valid options and correct_answer
    - Balanced answer distribution
    """
    errors: List[str] = []
    success, data, err_msg = _safe_load_json(file_path)
    if not success:
        return False, [err_msg]

    if not isinstance(data, dict):
        return False, ["NEDV file root must be a JSON object with 'items'"]

    items = data.get("items", [])
    if not isinstance(items, list) or len(items) != 6:
        errors.append(f"NEDV control expected 6 items, got {len(items) if isinstance(items, list) else 0}")
        return False, errors

    seen_ids: Set[str] = set()
    voip_count = 0
    fo_count = 0
    ans_keys: List[str] = []

    for item in items:
        item_id = item.get("id", "UNKNOWN")
        if item_id in seen_ids:
            errors.append(f"Duplicate NEDV item ID: '{item_id}'")
        seen_ids.add(item_id)

        prompt = item.get("prompt")
        if not prompt or not str(prompt).strip():
            errors.append(f"{item_id}: Empty prompt text")

        opts = item.get("options", {})
        if not isinstance(opts, dict) or len(opts) < 4:
            errors.append(f"{item_id}: Expected at least 4 options")

        ans = item.get("correct_answer")
        if ans not in opts:
            errors.append(f"{item_id}: correct_answer '{ans}' not found in options")
        else:
            ans_keys.append(ans)

        element = str(item.get("curriculum_element", "")).lower()
        if "voip" in element or "voice over ip" in element:
            voip_count += 1
        elif "fiber optik" in element or "fo" in element:
            fo_count += 1
        else:
            errors.append(f"{item_id}: Unrecognized NEDV curriculum element '{element}'")

    if voip_count != 2:
        errors.append(f"Expected 2 VoIP items (TP 2.3), got {voip_count}")
    if fo_count != 4:
        errors.append(f"Expected 4 Fiber Optik items (TP 2.4/2.5), got {fo_count}")

    # No single answer should dominate (> 3 out of 6)
    key_counts = collections.Counter(ans_keys)
    for opt, cnt in key_counts.items():
        if cnt > 3:
            errors.append(f"NEDV: Option '{opt}' overrepresented ({cnt}/6)")

    return len(errors) == 0, errors


def run_full_validation() -> bool:
    """Runs full validation suite and returns True if all pass, False otherwise."""
    logger.info("Validating Adaptive Bank (180 Items)...")
    ok1, err1 = validate_adaptive_bank()
    if not ok1:
        for e in err1[:5]:
            logger.error(f"  Adaptive Bank: {e}")

    logger.info("Validating Parallel TOLT Tests (A & B)...")
    ok2, err2 = validate_tolt_parallel_test()
    if not ok2:
        for e in err2[:5]:
            logger.error(f"  TOLT: {e}")

    logger.info("Validating Parallel Troubleshooting Tests Jonassen 2006 (36 Items A & B)...")
    ok_tb, err_tb = validate_troubleshooting_parallel_test()
    if not ok_tb:
        for e in err_tb[:5]:
            logger.error(f"  Troubleshooting Test: {e}")

    logger.info("Validating NEDV Control Items (6 Items)...")
    ok3, err3 = validate_nedv_controls()
    if not ok3:
        for e in err3[:5]:
            logger.error(f"  NEDV: {e}")

    all_ok = ok1 and ok2 and ok_tb and ok3
    if all_ok:
        logger.info("All L2 item bank integrity checks PASSED successfully.")
    else:
        logger.error("Item bank integrity checks FAILED.")
    return all_ok


if __name__ == "__main__":
    success = run_full_validation()
    sys.exit(0 if success else 1)
