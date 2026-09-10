from inventory import get_last_n_items

def test_get_last_n_items():
    assert get_last_n_items([1, 2, 3, 4, 5], 3) == [3, 4, 5]
    assert get_last_n_items([1, 2, 3], 1) == [3]
    assert get_last_n_items([10, 20], 2) == [10, 20]
