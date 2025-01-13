import assignment_1

def test_get_not_in():
    assert assignment_1.get_not_in(1, [1, 2, 3]) == False
    assert assignment_1.get_not_in(0, [1, 2, 3]) == True
    assert assignment_1.get_not_in('a', 'test') == True
    assert assignment_1.get_not_in('e', 'test') == False