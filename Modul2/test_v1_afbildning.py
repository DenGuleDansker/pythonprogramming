from pytest import raises
from v1_afbildning import increment, double, squared, lengths

# Test cases for the functions in v1_afbildning.py

def test_increment_raise_error():
    with raises(ValueError):
        increment([])

def test_increment_with_3_positives():
    assert increment([1, 2, 3]) == [2, 3, 4]

def test_increment_with_0():
    assert increment([0, 0, 0]) == [1, 1, 1]

def test_increment_with_negatives():
    assert increment([-1, -2]) == [0, -1]

def test_double_raise_error():
    with raises(ValueError):
        double([])

def test_double_with_3_positives():
    assert double([1, 2, 3]) == [2, 4, 6]

def test_double_with_0():
    assert double([0, 0, 0]) == [0, 0, 0]

def test_double_with_negatives():
    assert double([-1, -2, -3]) == [-2, -4, -6]

def test_squared_raises_error():
    with raises(ValueError):
        squared([])

def test_squared_in_place():
    # Arrange: Definer inputlisten
    input_list = [1, 2, 3]
    expected_list = [1, 4, 9]  # Definer det forventede resultat, da listen ændres in-place

    # Act: Kald funktionen der skal testes, `squared`, med inputlisten.  Listen modificeres direkte.
    squared(input_list)

    # Assert: Tjek om den *oprindelige* inputliste nu er som forventet.
    assert input_list == expected_list
    
def test_squared_with_0():
    assert squared([0, 0, 0]) == [0, 0, 0]

def test_squared_with_negatives():
    assert squared([-1, -2, -3]) == [1, 4, 9]

def test_squared_with_one_element():
    assert squared([10]) == [100]

def test_lengths():
    assert lengths(["abc", "ab", "a"]) == [3, 2, 1]
    assert lengths(["", "", ""]) == [0, 0, 0]