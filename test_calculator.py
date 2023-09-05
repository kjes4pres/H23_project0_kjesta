import pytest 

from calculator import add

@pytest.mark.parametrize(
        "x, y, expected", [(1, 2, 3), (2, 2, 4), (1, 1, 2)]
)
def test_add(x, y, expected):
    computed = add(x, y)
    success = computed == expected
    message = f"Computed value was {computed}, expected value was {expected}."
    assert success, message
