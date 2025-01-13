import assignment_1

def test_get_logical_or():
    assert assignment_1.get_logical_or(True, True) == True
    assert assignment_1.get_logical_or(False, True) == True
    assert assignment_1.get_logical_or(True, False) == True
    assert assignment_1.get_logical_or(False, False) == False
    assert assignment_1.get_logical_or(1, 2) == 3
    assert assignment_1.get_logical_or(1, 1) == 1
    assert assignment_1.get_logical_or(1, 3) == 3