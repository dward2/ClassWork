def test_add():
    from calculator import add
    answer = add(2, 3)
    expected = 5
    assert answer == expected
