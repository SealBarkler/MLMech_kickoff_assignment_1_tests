import assignment_1

def test_get_smaller_equal():
    assert assignment_1.get_smaller_equal(1, 3) == True
    assert assignment_1.get_smaller_equal(3, 1) == False
    assert assignment_1.get_smaller_equal(3, 3) == True
    assert assignment_1.get_smaller_equal('a', 'b') == True
    assert assignment_1.get_smaller_equal('b', 'a') == False
    assert assignment_1.get_smaller_equal('a', 'a') == True