from src.curry_uncurry import sum_args, curry, uncurry
import pytest

def test_curry():
    sum3_curry = curry(sum_args, 3)
    assert sum3_curry(1)(2)(3) == 6
    
def test_uncurry():
    sum3_curry = curry(sum_args, 3)
    sum3_curry(1)(2)(3)
    sum3_uncurry = uncurry(sum3_curry, 3)
    assert sum3_uncurry(1, 2, 3) == 6