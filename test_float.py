import pytest
import math as m

from calculator import add

@pytest.mark.parametrize(
        "x, y, expected", [(0.1, 0.2, 0.3), (0.2, 0.2, 0.4), (0.1, 0.1, 0.2)]
)
def test_float(x, y, expected):
    computed = add(x, y)
    success = m.isclose(expected, computed) == True
    message = f"Computed value was {computed}, expected value was {expected}."
    assert success, message