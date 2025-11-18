def test_a1():
    assert 4 < 5

def test_a2():
    assert 4 != 3

def test_a3():
    assert 'abc' == ('abcd')

def test_a4():
    assert 1 in divmod(9, 5)
    assert 'py' in 'this is pytest'