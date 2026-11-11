"""
LogiTrace: ZPD (Zone of Proximal Development) Adaptive Item Selector.
Implements the selection penalty function and DAG prerequisite gating from PRD §4.1.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Set
from .cognitive import calculate_predicted_p

TARGET_P: float = 0.72
ZPD_P_MIN: float = 0.60
ZPD_P_MAX: float = 0.85
PREREQUISITE_THRESHOLD: float = 0.60


@dataclass
class ItemCandidate:
    id: str
    primary_kc: str
    difficulty: int
    is_calibration: bool = False


class ZPDSelector:
    def __init__(self, dag_edges: List[Dict[str, str]]):
        """
        Initializes selector with DAG prerequisite dependencies.
        dag_edges format: [{'from': 'PARENT_KC', 'to': 'CHILD_KC'}, ...]
        """
        self.prerequisites: Dict[str, Set[str]] = {}
        for edge in dag_edges:
            parent = edge["from"]
            child = edge["to"]
            if child not in self.prerequisites:
                self.prerequisites[child] = set()
            self.prerequisites[child].add(parent)

    def are_prerequisites_met(
        self,
        kc_id: str,
        student_mastery: Dict[str, float]
    ) -> bool:
        """
        Returns True if all direct parents of kc_id have mastery >= PREREQUISITE_THRESHOLD (0.60).
        Root KCs have no prerequisites and always return True.
        """
        required_parents = self.prerequisites.get(kc_id, set())
        for parent_kc in required_parents:
            parent_m = student_mastery.get(parent_kc, 0.25)
            if parent_m < PREREQUISITE_THRESHOLD:
                return False
        return True

    def calculate_penalty_score(
        self,
        p_hat: float,
        kc_id: str,
        last_kc_id: Optional[str],
        touched_kcs: Set[str]
    ) -> float:
        """
        Calculates penalty score according to PRD formula:
            Score(q) = |p_hat(q) - 0.72| 
                       - 0.05 * I(KC untouched) 
                       + 0.10 * I(KC same as previous item)
        Lower score is better.
        """
        distance_to_target = abs(p_hat - TARGET_P)
        untouched_bonus = 0.05 if (kc_id not in touched_kcs) else 0.0
        consecutive_penalty = 0.10 if (last_kc_id is not None and kc_id == last_kc_id) else 0.0

        return distance_to_target - untouched_bonus + consecutive_penalty

    def select_next_item(
        self,
        candidate_items: List[ItemCandidate],
        student_mastery: Dict[str, float],
        answered_item_ids: Set[str],
        last_kc_id: Optional[str] = None,
        allow_relaxation: bool = True
    ) -> Optional[ItemCandidate]:
        """
        Selects the optimal candidate item minimizing the penalty function within the ZPD band.
        If strict ZPD yields no candidates, gracefully relaxes bounds if allow_relaxation is True.
        """
        # 1. Filter out already answered items
        unanswered = [
            item for item in candidate_items 
            if item.id not in answered_item_ids and not item.is_calibration
        ]
        if not unanswered:
            return None

        # 2. Filter by DAG prerequisites
        eligible = [
            item for item in unanswered
            if self.are_prerequisites_met(item.primary_kc, student_mastery)
        ]
        if not eligible:
            # If no items have satisfied prerequisites, pick an available root item
            eligible = unanswered

        # Determine touched KCs
        touched_kcs = {
            item.primary_kc for item in candidate_items 
            if item.id in answered_item_ids
        }

        # 3. Filter candidates within strict ZPD band [0.60, 0.85]
        zpd_candidates = []
        for item in eligible:
            kc_m = student_mastery.get(item.primary_kc, 0.25)
            p_hat = calculate_predicted_p(kc_m, item.difficulty)
            if ZPD_P_MIN <= p_hat <= ZPD_P_MAX:
                penalty = self.calculate_penalty_score(p_hat, item.primary_kc, last_kc_id, touched_kcs)
                zpd_candidates.append((penalty, item))

        if zpd_candidates:
            # Sort by ascending penalty score
            zpd_candidates.sort(key=lambda x: x[0])
            return zpd_candidates[0][1]

        # 4. Fallback relaxation if no item in strict band
        if allow_relaxation:
            relaxed_candidates = []
            for item in eligible:
                kc_m = student_mastery.get(item.primary_kc, 0.25)
                p_hat = calculate_predicted_p(kc_m, item.difficulty)
                penalty = self.calculate_penalty_score(p_hat, item.primary_kc, last_kc_id, touched_kcs)
                relaxed_candidates.append((penalty, item))
            
            if relaxed_candidates:
                relaxed_candidates.sort(key=lambda x: x[0])
                return relaxed_candidates[0][1]

        return None
