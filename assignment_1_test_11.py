import assignment_1

def test_get_logical_and():
    assert assignment_1.get_logical_and(True, True) == True
    assert assignment_1.get_logical_and(False, True) == False
    assert assignment_1.get_logical_and(True, False) == False
    assert assignment_1.get_logical_and(False, False) == False
    assert assignment_1.get_logical_and(1, 2) == 0
    assert assignment_1.get_logical_and(1, 1) == 1
    assert assignment_1.get_logical_and(1, 3) == 1