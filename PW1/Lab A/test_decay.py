"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


# TODO 1: test_rejects_negative_rate
#   Check that calling simulate(...) with a negative lam raises a ValueError.
#   Which pytest tool checks that an error is raised?


# TODO 2: test_matches_law
#   Check that the simulation's AVERAGE over many seeds is close to the
#   physical law  N0 * exp(-lam * t).
#   Which pytest tool compares floating-point values with a tolerance?
def test_rejects_negative_rate():
    # a negative decay rate is physically meaningless
    with pytest.raises(ValueError):
        simulate(1000, -0.1)


def test_matches_law():
    # the average over many seeds should follow N0 * exp(-lam * t)
    N0, lam, dt = 10000, 0.4, 0.05
    k = 100                  # check the value after 100 steps
    t = k * dt               # the corresponding time (5.0)
    runs = [simulate(N0, lam, dt=dt, seed=s)[k] for s in range(200)]
    average = np.mean(runs)
    expected = N0 * np.exp(-lam * t)
    assert average == pytest.approx(expected, rel=0.05)