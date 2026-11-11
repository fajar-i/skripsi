"""
LogiTrace: Deterministic Cognitive Engine (L3 Runtime Engine).
Implements the exact mathematical formulas specified in PRD §4.1 & Desain Final §3.
"""

from dataclasses import dataclass
import math
from typing import Dict, Optional

# A priori heuristic baseline parameters (calibrated in empirical trials)
ALPHA_0: float = 0.30
GAMMA_0: float = 0.25
BETA: float = 0.40

# Difficulty weights theta_d
THETA_MAP: Dict[int, float] = {
    1: +0.9,  # Easy
    2: 0.0,   # Medium
    3: -0.9   # Hard
}

# Mastery clipping boundaries
M_MIN: float = 0.02
M_MAX: float = 0.98

# Ebbinghaus temporal decay constant (in days)
TAU_DAYS: float = 60.0


def logit(m: float) -> float:
    """Calculates logit(m) = ln(m / (1 - m)) with boundary safety clipping."""
    safe_m = min(max(m, M_MIN), M_MAX)
    return math.log(safe_m / (1.0 - safe_m))


def sigmoid(z: float) -> float:
    """Calculates standard logistic sigmoid function sigma(z) = 1 / (1 + exp(-z))."""
    if z >= 40.0:
        return 1.0
    if z <= -40.0:
        return 0.0
    return 1.0 / (1.0 + math.exp(-z))


def calculate_predicted_p(mastery: float, difficulty: int) -> float:
    """
    Computes predicted probability of success p_hat(q) on an item:
        p_hat(q) = sigma(logit(m_{s, k_q}) + theta_{d_q})
    """
    theta = THETA_MAP.get(difficulty, 0.0)
    logit_m = logit(mastery)
    return sigmoid(logit_m + theta)


def get_alpha_d(difficulty: int, alpha_0: float = ALPHA_0, beta: float = BETA) -> float:
    """
    Learning rate adaptive to item difficulty:
        alpha_d = alpha_0 * (1 + beta * (d - 1))
    """
    return alpha_0 * (1.0 + beta * (difficulty - 1))


def get_gamma_d(difficulty: int, gamma_0: float = GAMMA_0, beta: float = BETA) -> float:
    """
    Slip penalty rate adaptive to item difficulty:
        gamma_d = gamma_0 * (1 + beta * (3 - d))
    """
    return gamma_0 * (1.0 + beta * (3 - difficulty))


def update_mastery(
    current_m: float,
    response_result: int,
    difficulty: int,
    used_hint: bool = False,
    alpha_0: float = ALPHA_0,
    gamma_0: float = GAMMA_0,
    beta: float = BETA,
) -> float:
    """
    Deterministic Mastery Update Rule:
        m <- m + alpha_d * (1 - m) * h   (if correct: r = 1)
        m <- m - gamma_d * m             (if incorrect: r = 0)
    
    where:
        h = 0.5 if hint was opened, else 1.0
        m is strictly clipped to [M_MIN, M_MAX] = [0.02, 0.98]
    """
    # Assistance factor h
    h = 0.5 if used_hint else 1.0

    if response_result == 1:
        alpha_d = get_alpha_d(difficulty, alpha_0, beta)
        new_m = current_m + alpha_d * (1.0 - current_m) * h
    else:
        gamma_d = get_gamma_d(difficulty, gamma_0, beta)
        new_m = current_m - gamma_d * current_m

    # Strict clipping to [0.02, 0.98]
    return min(max(new_m, M_MIN), M_MAX)


def apply_temporal_decay(
    m_last: float,
    elapsed_days: float,
    tau_k: float = TAU_DAYS
) -> float:
    """
    Ebbinghaus Memory Retention Decay (On-Read):
        m_k(t) = m_k(t_last) * exp(- (t - t_last) / tau_k)
    """
    if elapsed_days <= 0:
        return min(max(m_last, M_MIN), M_MAX)
    decayed = m_last * math.exp(-elapsed_days / tau_k)
    return min(max(decayed, M_MIN), M_MAX)
