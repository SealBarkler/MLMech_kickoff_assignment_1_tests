import assignment_1

def test_get_equal():
    assert assignment_1.get_equal(1, 1) == True
    assert assignment_1.get_equal(1, 2) == False
    assert assignment_1.get_equal(2, 1) == False
    assert assignment_1.get_equal('a', 'a') == True
    assert assignment_1.get_equal('a', 'b') == False
    assert assignment_1.get_equal(True, True) == True
    assert assignment_1.get_equal(True, False) == False