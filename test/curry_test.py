from src.curry_uncurry import sum_args, curry, uncurry
import pytest

def test_curry():
    sum3_curry = curry(sum_args, 3)
    assert sum3_curry(1)(2)(3) == 6
    
def test_uncurry():
    sum4_curry = curry(sum_args, 4)
    sum4_uncurry = uncurry(sum4_curry, 4)
    assert sum4_uncurry(1, 2, 3, 4) == 10