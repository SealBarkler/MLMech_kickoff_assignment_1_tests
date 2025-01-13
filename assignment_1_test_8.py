import assignment_1

def test_get_or():
    assert assignment_1.get_or(True, True) == True
    assert assignment_1.get_or(False, True) == True
    assert assignment_1.get_or(True, False) == True
    assert assignment_1.get_or(False, False) == False