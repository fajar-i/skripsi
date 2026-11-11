"""
Unit Tests for Cold-Start Calibration Manager (US-01).
Verifies initial prior (0.25), 6-item standardized sequence, and prerequisite cluster estimation.
"""

import pytest
from backend.app.engine.calibration import (
    CalibrationManager,
    CalibrationItem,
    INITIAL_PRIOR_M,
    CALIBRATION_TOTAL_ITEMS
)


@pytest.fixture
def manager():
    all_kcs = [
        "WLAN_STANDARDS", "WLAN_TOPOLOGY_BSS", "IP_PEER_CONFIG",
        "WLAN_FREQ_CHANNEL", "WLAN_SECURITY_AUTH", "ICMP_CONNECTIVITY"
    ]
    return CalibrationManager(all_kcs)


def test_initial_prior_mastery(manager):
    """All KCs must start at prior 0.25 for cold-start students."""
    mastery = manager.initialize_student_mastery()
    assert len(mastery) == 6
    assert all(m == INITIAL_PRIOR_M for m in mastery.values())


def test_is_calibrating_threshold(manager):
    """Calibration must be active for first 6 items only."""
    assert manager.is_calibrating(0) is True
    assert manager.is_calibrating(5) is True
    assert manager.is_calibrating(6) is False
    assert manager.is_calibrating(10) is False


def test_estimate_unmeasured_kcs_confidence_flags(manager):
    """Measured KCs have high confidence; unmeasured KCs have low confidence."""
    current_m = {
        "WLAN_STANDARDS": 0.70,
        "WLAN_TOPOLOGY_BSS": 0.60,
        "IP_PEER_CONFIG": 0.50,
        "WLAN_FREQ_CHANNEL": 0.25,
        "WLAN_SECURITY_AUTH": 0.25,
        "ICMP_CONNECTIVITY": 0.25,
    }
    measured = {"WLAN_STANDARDS", "WLAN_TOPOLOGY_BSS", "IP_PEER_CONFIG"}
    edges = [
        {"from": "WLAN_STANDARDS", "to": "WLAN_FREQ_CHANNEL"},
        {"from": "IP_PEER_CONFIG", "to": "WLAN_SECURITY_AUTH"},
    ]

    estimations = manager.estimate_unmeasured_kcs(current_m, measured, edges)

    assert estimations["WLAN_STANDARDS"]["confidence"] == "high"
    assert estimations["WLAN_FREQ_CHANNEL"]["confidence"] == "low"
    # Unmeasured child estimation inherits from parent:
    assert pytest.approx(estimations["WLAN_FREQ_CHANNEL"]["m"], abs=1e-3) == 0.70


def test_balanced_6_item_calibration_sequence(manager):
    """
    When 9 calibration items exist (3 root KCs x 3 difficulties),
    get_next_calibration_item must select a balanced 6-item sequence:
    2 easy (diff 1), 2 medium (diff 2), 2 hard (diff 3), and 2 per root KC.
    """
    root_kcs = ["WLAN_STANDARDS", "WLAN_TOPOLOGY_BSS", "IP_PEER_CONFIG"]
    bank = []
    for kc in root_kcs:
        for diff in (1, 2, 3):
            bank.append(CalibrationItem(id=f"CAL_{kc}_{diff}", primary_kc=kc, difficulty=diff, is_calibration=True))

    answered = set()
    selected = []
    for _ in range(6):
        nxt = manager.get_next_calibration_item(bank, answered)
        assert nxt is not None
        selected.append(nxt)
        answered.add(nxt.id)

    assert len(selected) == 6
    diff_counts = {1: 0, 2: 0, 3: 0}
    kc_counts = {kc: 0 for kc in root_kcs}
    for it in selected:
        diff_counts[it.difficulty] += 1
        kc_counts[it.primary_kc] += 1

    assert diff_counts == {1: 2, 2: 2, 3: 2}
    assert kc_counts == {"WLAN_STANDARDS": 2, "WLAN_TOPOLOGY_BSS": 2, "IP_PEER_CONFIG": 2}
