from Modul1.smallest import smallest_two, INFINITY

INFINITY = float('inf')

def test_smallest_empty():
    assert smallest_two([]) == (INFINITY, INFINITY)

def test_smallest_single():
    assert smallest_two([7]) == (7, INFINITY)

def test_smallest_two():
    assert smallest_two([7, 3]) == (3, 7)
    assert smallest_two([7, 7]) == (7, 7)  

def test_smallest_three():
    assert smallest_two([8, 7, 3]) == (3, 7)
