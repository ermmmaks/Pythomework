import math
from src.walker import WalkersAlias

N_TESTS = 100000
INACCURACY = 0.01

def test_same_distribution():
    distribution = [("A", 0.5), ("B", 0.5)]
    walker = WalkersAlias(distribution)
    results = {"A": 0, "B": 0}

    for _ in range(N_TESTS):
        event = walker.get_random()
        results[event] += 1

    assert math.isclose(results["A"] / N_TESTS, 0.5, abs_tol=INACCURACY)
    assert math.isclose(results["B"] / N_TESTS, 0.5, abs_tol=INACCURACY)
    
def test_multiple_events():
    distribution = [("A", 0.65), ("B", 0.1), ("C", 0.2), ("D", 0.05)]
    walker = WalkersAlias(distribution)
    results = {e: 0 for e, p in distribution}

    for _ in range(N_TESTS):
        event = walker.get_random()
        results[event] += 1

    assert math.isclose(results["A"] / N_TESTS, 0.65, abs_tol=INACCURACY)
    assert math.isclose(results["B"] / N_TESTS, 0.1, abs_tol=INACCURACY)
    assert math.isclose(results["C"] / N_TESTS, 0.2, abs_tol=INACCURACY)
    assert math.isclose(results["D"] / N_TESTS, 0.05, abs_tol=INACCURACY)

def test_inaccuracy():
    p = 0.1
    distribution = [("A", p)] * 10
    walker = WalkersAlias(distribution)

    assert walker.ln == 10