import assignment_1

def test_get_xor():
    assert assignment_1.get_logical_and(True, True) == False
    assert assignment_1.get_logical_and(False, True) == True
    assert assignment_1.get_logical_and(True, False) == True
    assert assignment_1.get_logical_and(False, False) == False
    assert assignment_1.get_logical_and(1, 2) == 3
    assert assignment_1.get_logical_and(1, 1) == 0
    assert assignment_1.get_logical_and(1, 3) == 2