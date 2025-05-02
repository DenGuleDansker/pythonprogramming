from v2_reduktion import sum_of, concat_of, prod_of

def test_raise_to_zero():
    assert sum_of([]) == 0

def test_sum_of_single():
    assert sum_of([7]) == 7

def test_sum_of_two():
    assert sum_of([7, 3]) == 10
    assert sum_of([7, 7]) == 14

def test_sum_of_three():
    assert sum_of([8, 7, 3]) == 18
    assert sum_of([8, 7, 7]) == 22


