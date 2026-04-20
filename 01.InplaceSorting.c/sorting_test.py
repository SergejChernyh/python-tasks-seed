"""
Unit tests for 01.InplaceSorting
"""

import random
from itertools import pairwise
import pytest
import sortings
from counting_container import CountingList, CountingOrdered


@pytest.fixture(scope="module", name="data_array")
def data_array_fixture():
    """
    Create a shuffled array of 1000 elements with fixed seed
    """
    r = random.Random()
    r.seed(123456)
    raw_data = list(range(1000))
    r.shuffle(raw_data)

    CountingList.reset_stats()
    CountingOrdered.reset_stats()

    data = CountingList(list(map(CountingOrdered, raw_data)))

    yield data


def test_trivial_sort2():
    """
    Test trivial sorting of a 2-element array
    """

    a2 = CountingList(list(map(CountingOrdered, [2, 1])))
    sortings.trivial_sort2(a2)
    assert CountingList.likely_swaps() == 1, "Number of swaps for array [2, 1] is not 1"
    assert (
        CountingOrdered.comparisons() == 1
    ), "Number of comparisons for array [2, 1] is not 1"
    assert all(x <= y for x, y in pairwise(a2)), "Array [2, 1] is not sorted"


@pytest.mark.parametrize("_name, sort_func", sortings.sorting_algs)
def test_all_sortings(data_array, _name, sort_func):
    """
    Verify that the sorting function correctly orders the array.
    """
    sort_func(data_array)
    assert all(x <= y for x, y in pairwise(data_array))
