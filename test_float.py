import math as m

from calculator import add


def test_float():
    x = 0.1
    y = 0.2
    expected = 0.3
    computed = add(x, y)
    success = m.isclose(expected,computed) == True
    message = f"computed value was {computed}, expected value was {expected}"
    assert success, message