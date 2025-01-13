import assignment_1

def test_get_bigger_equal():
    assert assignment_1.get_bigger_equal(1, 3) == False
    assert assignment_1.get_bigger_equal(3, 1) == True
    assert assignment_1.get_bigger_equal(3, 3) == True
    assert assignment_1.get_bigger_equal('a', 'b') == False
    assert assignment_1.get_bigger_equal('b', 'a') == True
    assert assignment_1.get_bigger_equal('a', 'a') == True