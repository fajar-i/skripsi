"""
Unit Tests for ZPD Adaptive Item Selector.
Verifies penalty function, ZPD band filtering [0.60, 0.85], and DAG prerequisite gating.
"""

import pytest
from backend.app.engine.zpd_selector import ZPDSelector, ItemCandidate


@pytest.fixture
def sample_dag_edges():
    return [
        {"from": "WLAN_STANDARDS", "to": "WLAN_FREQ_CHANNEL"},
        {"from": "WLAN_FREQ_CHANNEL", "to": "WLAN_CHANNEL_COLLISION"},
    ]


def test_prerequisite_gating(sample_dag_edges):
    """Child KC items must be blocked until all direct parents reach mastery >= 0.60."""
    selector = ZPDSelector(sample_dag_edges)

    # 1. Root KC has no prerequisites
    assert selector.are_prerequisites_met("WLAN_STANDARDS", {}) is True

    # 2. Child KC with parent mastery < 0.60 -> False
    mastery = {"WLAN_STANDARDS": 0.45}
    assert selector.are_prerequisites_met("WLAN_FREQ_CHANNEL", mastery) is False

    # 3. Child KC with parent mastery >= 0.60 -> True
    mastery = {"WLAN_STANDARDS": 0.65}
    assert selector.are_prerequisites_met("WLAN_FREQ_CHANNEL", mastery) is True

    # 4. Grandchild KC with grandparent >= 0.60 but parent < 0.60 -> False
    mastery = {"WLAN_STANDARDS": 0.80, "WLAN_FREQ_CHANNEL": 0.50}
    assert selector.are_prerequisites_met("WLAN_CHANNEL_COLLISION", mastery) is False


def test_zpd_selection_within_band(sample_dag_edges):
    """Selector chooses item with p_hat closest to 0.72 within [0.60, 0.85]."""
    selector = ZPDSelector(sample_dag_edges)

    candidates = [
        # At mastery 0.50:
        # Easy (diff 1): p_hat ~ 0.7109 (|0.7109 - 0.72| = 0.0091)
        # Medium (diff 2): p_hat = 0.50 (outside [0.60, 0.85])
        # Hard (diff 3): p_hat ~ 0.2891 (outside)
        ItemCandidate(id="item_easy", primary_kc="WLAN_STANDARDS", difficulty=1),
        ItemCandidate(id="item_med", primary_kc="WLAN_STANDARDS", difficulty=2),
        ItemCandidate(id="item_hard", primary_kc="WLAN_STANDARDS", difficulty=3),
    ]

    mastery = {"WLAN_STANDARDS": 0.50}
    selected = selector.select_next_item(
        candidate_items=candidates,
        student_mastery=mastery,
        answered_item_ids=set(),
        last_kc_id=None
    )

    assert selected is not None
    assert selected.id == "item_easy"


def test_consecutive_kc_penalty_and_untouched_bonus(sample_dag_edges):
    """Items from untouched KCs get -0.05 bonus; consecutive items get +0.10 penalty."""
    selector = ZPDSelector(sample_dag_edges)

    # Let's test score calculation directly
    # Candidate A: untouched KC, p_hat = 0.75 -> |0.75 - 0.72| - 0.05 + 0 = 0.03 - 0.05 = -0.02
    score_a = selector.calculate_penalty_score(
        p_hat=0.75,
        kc_id="KC_A",
        last_kc_id=None,
        touched_kcs=set()
    )
    assert pytest.approx(score_a, abs=1e-4) == -0.02

    # Candidate B: consecutive same KC, p_hat = 0.72 -> |0.72 - 0.72| + 0.10 = 0.10
    score_b = selector.calculate_penalty_score(
        p_hat=0.72,
        kc_id="KC_B",
        last_kc_id="KC_B",
        touched_kcs={"KC_B"}
    )
    assert pytest.approx(score_b, abs=1e-4) == 0.10
