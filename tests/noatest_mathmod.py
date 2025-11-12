

import mathmod

def test_simple_add():

    answer = mathmod.add(1, 1)
    assert answer == 2

def test_decimal_add():
    answer = mathmod.add(0.1, 0.2)
    #assert answer == 0.3
    assert round(answer, 1) == 0.3

def test_simple_div():
    answer = 3 / 3

    assert answer == 1