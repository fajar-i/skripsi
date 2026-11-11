"""
Unit Tests for Deterministic L3 Cognitive Engine.
Verifies formulas for p_hat, mastery updates, boundary constraints [0.02, 0.98],
hint penalty h=0.5, and temporal decay.
"""

import math
import pytest
from backend.app.engine.cognitive import (
    calculate_predicted_p,
    update_mastery,
    apply_temporal_decay,
    logit,
    sigmoid,
    M_MIN,
    M_MAX,
    ALPHA_0,
    GAMMA_0,
    BETA,
    THETA_MAP
)


def test_logit_and_sigmoid_inversion():
    """logit and sigmoid should be inverse functions within safe boundaries."""
    m = 0.65
    z = logit(m)
    recovered = sigmoid(z)
    assert pytest.approx(recovered, abs=1e-5) == m


def test_predicted_p_monotonicity_with_difficulty():
    """For identical mastery, p_hat must decrease as difficulty increases."""
    mastery = 0.50
    p_easy = calculate_predicted_p(mastery, difficulty=1)
    p_med = calculate_predicted_p(mastery, difficulty=2)
    p_hard = calculate_predicted_p(mastery, difficulty=3)

    assert p_easy > p_med > p_hard
    # At m = 0.50, logit(0.5) = 0.
    # Therefore p_easy = sigmoid(0 + 0.9) = 1 / (1 + exp(-0.9)) = ~0.7109
    # p_med = sigmoid(0 + 0.0) = 0.50
    # p_hard = sigmoid(0 - 0.9) = ~0.2891
    assert pytest.approx(p_med, abs=1e-3) == 0.50
    assert p_easy > 0.70
    assert p_hard < 0.30


def test_update_mastery_correct_without_hint():
    """Correct response (r=1) without hint (h=1.0) increases mastery proportionally."""
    initial_m = 0.50
    difficulty = 2  # medium: alpha_d = alpha_0 * (1 + 0.40 * 1) = 0.30 * 1.40 = 0.42
    new_m = update_mastery(initial_m, response_result=1, difficulty=difficulty, used_hint=False)

    # Expected: m + 0.42 * (1 - 0.50) * 1.0 = 0.50 + 0.21 = 0.71
    assert pytest.approx(new_m, abs=1e-4) == 0.71
    assert new_m > initial_m


def test_update_mastery_correct_with_hint_penalty():
    """Correct response with hint (h=0.5) yields exactly half the gain."""
    initial_m = 0.50
    difficulty = 2
    new_m_hint = update_mastery(initial_m, response_result=1, difficulty=difficulty, used_hint=True)
    new_m_no_hint = update_mastery(initial_m, response_result=1, difficulty=difficulty, used_hint=False)

    gain_hint = new_m_hint - initial_m
    gain_no_hint = new_m_no_hint - initial_m

    assert pytest.approx(gain_hint, abs=1e-4) == gain_no_hint * 0.5


def test_update_mastery_incorrect_penalty():
    """Incorrect response (r=0) decreases mastery based on gamma_d."""
    initial_m = 0.50
    difficulty = 1  # easy: gamma_d = gamma_0 * (1 + beta * (3 - 1)) = 0.25 * (1 + 0.8) = 0.45
    new_m = update_mastery(initial_m, response_result=0, difficulty=difficulty)

    # Expected: 0.50 - 0.45 * 0.50 = 0.50 - 0.225 = 0.275
    assert pytest.approx(new_m, abs=1e-4) == 0.275
    assert new_m < initial_m


def test_mastery_strict_clipping_boundaries():
    """Mastery value m MUST never exceed [0.02, 0.98] under extreme repetitions."""
    m = 0.95
    # 10 consecutive correct answers on hard items
    for _ in range(10):
        m = update_mastery(m, response_result=1, difficulty=3, used_hint=False)
    assert m <= M_MAX
    assert pytest.approx(m, abs=1e-4) == M_MAX

    # 10 consecutive wrong answers on easy items
    for _ in range(15):
        m = update_mastery(m, response_result=0, difficulty=1, used_hint=False)
    assert m >= M_MIN
    assert pytest.approx(m, abs=1e-4) == M_MIN


def test_ebbinghaus_temporal_decay():
    """Memory retention decays smoothly over elapsed days with tau = 60 days."""
    m_0 = 0.80
    m_30 = apply_temporal_decay(m_0, elapsed_days=30.0, tau_k=60.0)
    m_60 = apply_temporal_decay(m_0, elapsed_days=60.0, tau_k=60.0)

    # At 60 days (1 half-life constant tau): m = m_0 * exp(-1) = 0.80 * 0.367879 = ~0.2943
    assert m_0 > m_30 > m_60
    assert pytest.approx(m_60, abs=1e-3) == 0.80 * math.exp(-1.0)
