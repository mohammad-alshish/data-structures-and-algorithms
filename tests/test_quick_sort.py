from quick_sort.quick_sort import quick_sort


def test_empty_array():
    actual = quick_sort([], 0, 0)
    expected = []
    actual == expected


def test_positive_numbers():
    actual = quick_sort([5, 7, 9, 6, 1, 7, 4], 0, 6)
    expected = [1, 4, 5, 5, 6, 7, 7, 9]
    actual == expected


def test_negative_numbers():
    actual = quick_sort([-1, -5, -9, -7], 0, 3)
    expected = [-9, -7, -5, -1]
    actual == expected


def test_mixed_numbers():
    actual = quick_sort([0, 5, 2, -1, 7, 1000], 0, 5)
    expected = [-1, 0, 2, 5, 7, 1000]
    actual == expected
