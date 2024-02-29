from median import get_median
def test_median():
    print("Testing median")
    assert get_median([7, 1, 5, 3]) == 4
    print("Passed test 1")
    
test_median()