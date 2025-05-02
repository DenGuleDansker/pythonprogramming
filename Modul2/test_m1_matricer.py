from m1_matricer import matrix_double

def test_matricer_double():
    assert matrix_double([[5,2,5],[1,2,5]]) == [[10,4,10], [2,4,10]]

def test_matricer_double_negatives():
    assert matrix_double([[-1,-2,-3], [-2,-5,-6]]) == [[-2,-4,-6], [-4,-10,-12]]