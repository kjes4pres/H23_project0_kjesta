from calculator import add


def test_add():
    x = 1
    y = 2
    expected = 3
    computed = add(x, y)
    success = computed == expected
    message = f"computed value was {computed}, expected value was {expected}"
    assert success, message
