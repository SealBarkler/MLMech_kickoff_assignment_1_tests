import assignment_1

def test_get_bigger():
    assert assignment_1.get_bigger(1, 3) == False
    assert assignment_1.get_bigger(3, 1) == True
    assert assignment_1.get_bigger(3, 3) == False
    assert assignment_1.get_bigger('a', 'b') == False
    assert assignment_1.get_bigger('b', 'a') == True
    assert assignment_1.get_bigger('a', 'a') == False