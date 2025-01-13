import assignment_1

def test_get_in():
    assert assignment_1.get_in(1, [1, 2, 3]) == True
    assert assignment_1.get_in(0, [1, 2, 3]) == False
    assert assignment_1.get_in('a', 'test') == False
    assert assignment_1.get_in('e', 'test') == True