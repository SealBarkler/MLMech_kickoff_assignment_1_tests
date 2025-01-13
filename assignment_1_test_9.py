import assignment_1

def test_get_and():
    assert assignment_1.get_and(True, True) == True
    assert assignment_1.get_and(False, True) == False
    assert assignment_1.get_and(True, False) == False
    assert assignment_1.get_and(False, False) == False