import assignment_1

def test_get_not_equal():
    assert assignment_1.get_not_equal(1, 1) == False
    assert assignment_1.get_not_equal(1, 2) == True
    assert assignment_1.get_equal(2, 1) == True
    assert assignment_1.get_equal('a', 'a') == False
    assert assignment_1.get_equal('a', 'b') == True
    assert assignment_1.get_equal(True, True) == False
    assert assignment_1.get_equal(True, False) == True