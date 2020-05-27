def test_add():
    from calculator import add
    answer = add(1, 2)
    expected = 3
    assert answer == expected
