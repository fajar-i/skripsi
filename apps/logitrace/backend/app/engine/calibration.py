"""
LogiTrace: Cold-Start Calibration Protocol (US-01).
Handles the 6-item standardization protocol for new students.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Set

INITIAL_PRIOR_M: float = 0.25
CALIBRATION_TOTAL_ITEMS: int = 6
CALIBRATION_ROOT_KCS: List[str] = [
    "WLAN_STANDARDS",
    "WLAN_TOPOLOGY_BSS",
    "IP_PEER_CONFIG"
]


@dataclass
class CalibrationItem:
    id: str
    primary_kc: str
    difficulty: int  # 1: easy, 2: medium, 3: hard
    is_calibration: bool = True


class CalibrationManager:
    """Manages the 6-item calibration session for cold-start students."""

    def __init__(self, all_kc_ids: List[str]):
        self.all_kc_ids = all_kc_ids

    def initialize_student_mastery(self) -> Dict[str, float]:
        """Initializes all KCs to prior value 0.25."""
        return {kc_id: INITIAL_PRIOR_M for kc_id in self.all_kc_ids}

    def is_calibrating(self, answered_count: int) -> bool:
        """Returns True if the student is within the first 6 calibration items."""
        return answered_count < CALIBRATION_TOTAL_ITEMS

    def get_next_calibration_item(
        self,
        calibration_bank: List[CalibrationItem],
        answered_ids: Set[str]
    ) -> Optional[CalibrationItem]:
        """
        Retrieves the next unanswered calibration item from the standardized 6-item sequence:
        2 easy (diff 1), 2 medium (diff 2), 2 hard (diff 3) balanced across the 3 root KCs
        (WLAN_STANDARDS, WLAN_TOPOLOGY_BSS, IP_PEER_CONFIG).
        """
        if len(answered_ids) >= CALIBRATION_TOTAL_ITEMS:
            return None

        # Standardized 6-slot Latin-square schedule (2 per root KC, 2 per difficulty level)
        target_schedule = [
            ("WLAN_STANDARDS", 1),
            ("WLAN_TOPOLOGY_BSS", 1),
            ("IP_PEER_CONFIG", 2),
            ("WLAN_STANDARDS", 2),
            ("WLAN_TOPOLOGY_BSS", 3),
            ("IP_PEER_CONFIG", 3),
        ]

        unanswered = [
            item for item in calibration_bank
            if item.id not in answered_ids and item.is_calibration
        ]
        if not unanswered:
            return None

        # Count already answered KCs and difficulties from calibration_bank
        answered_items = [item for item in calibration_bank if item.id in answered_ids]
        kc_counts = {kc: 0 for kc in CALIBRATION_ROOT_KCS}
        diff_counts = {1: 0, 2: 0, 3: 0}
        for it in answered_items:
            if it.primary_kc in kc_counts:
                kc_counts[it.primary_kc] += 1
            if it.difficulty in diff_counts:
                diff_counts[it.difficulty] += 1

        # 1. Try matching the next unfilled slot in target_schedule
        for target_kc, target_diff in target_schedule:
            if kc_counts.get(target_kc, 0) < 2 and diff_counts.get(target_diff, 0) < 2:
                for item in unanswered:
                    if item.primary_kc == target_kc and item.difficulty == target_diff:
                        return item

        # 2. Fallback: pick unanswered item that minimizeskc_counts and diff_counts imbalance
        unanswered.sort(
            key=lambda it: (
                kc_counts.get(it.primary_kc, 99),
                diff_counts.get(it.difficulty, 99),
                it.difficulty
            )
        )
        return unanswered[0]

    def estimate_unmeasured_kcs(
        self,
        current_mastery: Dict[str, float],
        measured_kcs: Set[str],
        dag_edges: List[Dict[str, str]]
    ) -> Dict[str, Dict[str, any]]:
        """
        Estimates unmeasured KCs from prerequisite parent clusters.
        Returns a dictionary mapping kc_id -> {'m': float, 'confidence': 'low' | 'high'}.
        """
        result = {}
        for kc_id in self.all_kc_ids:
            if kc_id in measured_kcs:
                result[kc_id] = {
                    "m": current_mastery.get(kc_id, INITIAL_PRIOR_M),
                    "confidence": "high"
                }
            else:
                # Find direct parents in DAG
                parents = [e["from"] for e in dag_edges if e["to"] == kc_id]
                if parents:
                    parent_vals = [current_mastery.get(p, INITIAL_PRIOR_M) for p in parents]
                    avg_m = sum(parent_vals) / len(parent_vals)
                else:
                    avg_m = INITIAL_PRIOR_M
                
                result[kc_id] = {
                    "m": avg_m,
                    "confidence": "low"  # Displayed with striped pattern on teacher dashboard
                }
        return result
