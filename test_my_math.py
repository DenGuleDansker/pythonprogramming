from Modul1.my_math import exp

def test_raise_to_zero():
    assert exp(7, 0) == 1

def test_raise_to_one():
    assert exp(7, 1) == 7

def test_raise_to_two():
    assert exp(7, 2) == 49

def test_raise_to_high():
    assert exp(2, 11) == 2048

