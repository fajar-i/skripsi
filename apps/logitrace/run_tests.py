"""
Standalone test runner using Python standard library (unittest).
Executes cognitive engine, ZPD selector, guardrails, and calibration test suites.
"""

import sys
import os
import math
import unittest

# Ensure logitrace root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from backend.app.engine.cognitive import (
    calculate_predicted_p,
    update_mastery,
    apply_temporal_decay,
    logit,
    sigmoid,
    M_MIN,
    M_MAX
)
from backend.app.engine.zpd_selector import ZPDSelector, ItemCandidate
from backend.app.rag.guardrails import AnswerLeakageGuard, MAX_HINT_WORDS
from backend.app.engine.calibration import CalibrationManager, INITIAL_PRIOR_M
from tests.test_item_bank import TestItemBankIntegrity, TestItemBankNegativeEdgeCases


class TestCognitiveEngine(unittest.TestCase):
    def test_logit_and_sigmoid_inversion(self):
        m = 0.65
        z = logit(m)
        recovered = sigmoid(z)
        self.assertAlmostEqual(recovered, m, places=5)

    def test_predicted_p_monotonicity(self):
        mastery = 0.50
        p_easy = calculate_predicted_p(mastery, difficulty=1)
        p_med = calculate_predicted_p(mastery, difficulty=2)
        p_hard = calculate_predicted_p(mastery, difficulty=3)

        self.assertTrue(p_easy > p_med > p_hard)
        self.assertAlmostEqual(p_med, 0.50, places=3)
        self.assertGreater(p_easy, 0.70)
        self.assertLess(p_hard, 0.30)

    def test_update_mastery_correct_without_hint(self):
        initial_m = 0.50
        new_m = update_mastery(initial_m, response_result=1, difficulty=2, used_hint=False)
        self.assertAlmostEqual(new_m, 0.71, places=4)

    def test_update_mastery_correct_with_hint_penalty(self):
        initial_m = 0.50
        new_m_hint = update_mastery(initial_m, response_result=1, difficulty=2, used_hint=True)
        new_m_no_hint = update_mastery(initial_m, response_result=1, difficulty=2, used_hint=False)

        gain_hint = new_m_hint - initial_m
        gain_no_hint = new_m_no_hint - initial_m
        self.assertAlmostEqual(gain_hint, gain_no_hint * 0.5, places=4)

    def test_update_mastery_incorrect(self):
        initial_m = 0.50
        new_m = update_mastery(initial_m, response_result=0, difficulty=1)
        self.assertAlmostEqual(new_m, 0.275, places=4)

    def test_mastery_clipping_boundaries(self):
        m = 0.95
        for _ in range(10):
            m = update_mastery(m, response_result=1, difficulty=3, used_hint=False)
        self.assertAlmostEqual(m, M_MAX, places=4)

        for _ in range(15):
            m = update_mastery(m, response_result=0, difficulty=1, used_hint=False)
        self.assertAlmostEqual(m, M_MIN, places=4)

    def test_ebbinghaus_decay(self):
        m_0 = 0.80
        m_60 = apply_temporal_decay(m_0, elapsed_days=60.0, tau_k=60.0)
        self.assertAlmostEqual(m_60, 0.80 * math.exp(-1.0), places=3)


class TestZPDSelector(unittest.TestCase):
    def setUp(self):
        self.edges = [
            {"from": "WLAN_STANDARDS", "to": "WLAN_FREQ_CHANNEL"},
            {"from": "WLAN_FREQ_CHANNEL", "to": "WLAN_CHANNEL_COLLISION"},
        ]
        self.selector = ZPDSelector(self.edges)

    def test_prerequisite_gating(self):
        self.assertTrue(self.selector.are_prerequisites_met("WLAN_STANDARDS", {}))
        self.assertFalse(self.selector.are_prerequisites_met("WLAN_FREQ_CHANNEL", {"WLAN_STANDARDS": 0.45}))
        self.assertTrue(self.selector.are_prerequisites_met("WLAN_FREQ_CHANNEL", {"WLAN_STANDARDS": 0.65}))

    def test_zpd_selection(self):
        candidates = [
            ItemCandidate(id="item_easy", primary_kc="WLAN_STANDARDS", difficulty=1),
            ItemCandidate(id="item_med", primary_kc="WLAN_STANDARDS", difficulty=2),
            ItemCandidate(id="item_hard", primary_kc="WLAN_STANDARDS", difficulty=3),
        ]
        mastery = {"WLAN_STANDARDS": 0.50}
        selected = self.selector.select_next_item(
            candidate_items=candidates,
            student_mastery=mastery,
            answered_item_ids=set()
        )
        self.assertIsNotNone(selected)
        self.assertEqual(selected.id, "item_easy")


class TestGuardrails(unittest.TestCase):
    def setUp(self):
        self.guard = AnswerLeakageGuard()

    def test_clean_hint(self):
        hint = "Perhatikan perbedaan antara frekuensi 2.4 GHz dan 5 GHz."
        is_safe, _ = self.guard.check_leakage(hint, correct_answer="802.11ax")
        self.assertTrue(is_safe)

    def test_leakage_phrases(self):
        bad_hint = "Jawabannya adalah opsi kedua karena frekuensi lebih tinggi."
        is_safe, _ = self.guard.check_leakage(bad_hint, correct_answer="WPA3")
        self.assertFalse(is_safe)

    def test_direct_answer_leakage(self):
        bad_hint = "Pilihlah protokol WPA3-SAE untuk keamanan tinggi."
        is_safe, _ = self.guard.check_leakage(bad_hint, correct_answer="WPA3-SAE")
        self.assertFalse(is_safe)


class TestCalibration(unittest.TestCase):
    def setUp(self):
        self.manager = CalibrationManager(["KC_1", "KC_2", "KC_3"])

    def test_initialization(self):
        mastery = self.manager.initialize_student_mastery()
        self.assertEqual(len(mastery), 3)
        self.assertTrue(all(m == INITIAL_PRIOR_M for m in mastery.values()))

    def test_is_calibrating(self):
        self.assertTrue(self.manager.is_calibrating(0))
        self.assertTrue(self.manager.is_calibrating(5))
        self.assertFalse(self.manager.is_calibrating(6))


if __name__ == "__main__":
    unittest.main(verbosity=2)
