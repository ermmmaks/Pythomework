import pytest
import random

@pytest.fixture
def rndm():
    rndm_array = [random.randint(-100, 100) for i in range(10)]
    return rndm_array