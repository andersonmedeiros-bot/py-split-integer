from app.split_integer import split_integer


def test_example_from_description():
    assert split_integer(8, 1) == [8]
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_correct_number_of_elements():
    assert len(split_integer(10, 3)) == 3
    assert len(split_integer(100, 10)) == 10
    assert len(split_integer(2, 2)) == 2
    assert len(split_integer(11, 4)) == 4


def test_sorted_ascending():
    result1 = split_integer(17, 4)
    assert result1 == sorted(result1)

    result2 = split_integer(32, 6)
    assert result2 == sorted(result2)

    result3 = split_integer(11, 4)
    assert result3 == sorted(result3)


def test_max_min_difference():
    for v, p in [(17, 4), (32, 6), (11, 4), (6, 2), (8, 3)]:
        result = split_integer(v, p)
        assert max(result) - min(result) <= 1


def test_sum_equals_value():
    for v, p in [(17, 4), (32, 6), (11, 4), (6, 2), (8, 3), (100, 9)]:
        assert sum(split_integer(v, p)) == v
