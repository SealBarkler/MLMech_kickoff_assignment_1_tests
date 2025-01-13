import assignment_1

def test_get_smaller():
    assert assignment_1.get_smaller(1, 3) == True
    assert assignment_1.get_smaller(3, 1) == False
    assert assignment_1.get_smaller(3, 3) == False
    assert assignment_1.get_smaller('a', 'b') == True
    assert assignment_1.get_smaller('b', 'a') == False
    assert assignment_1.get_smaller('a', 'a') == False