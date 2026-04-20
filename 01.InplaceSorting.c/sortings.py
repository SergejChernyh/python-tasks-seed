"""
Sorting algorithms
"""

import sys
import inspect


def bubble_sort(data):
    """
    Bubble sort with checking and stoping if array is sorted

    :param data: data to sort inplace
    :type data: list[BasicType] or other indexable sequence[BasicType]
    """

    i = 0
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
                is_sorted = False
        i += 1


def selection_sort(data):
    """
    Performs a minimal number of writes to memory (__setitem__)

    :param data: data to sort inplace
    :type data: list[BasicType] or other indexable sequence[BasicType]
    """
    n = len(data)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j

        data[i], data[min_idx] = data[min_idx], data[i]

    return data


def quick_sort(data, low=0, high=None):
    """
    QuickSort with Hoare Partition Scheme

    :param data: data to sort inplace
    :type data: list[BasicType] or other indexable sequence[BasicType]
    """

    def partition_hoare(data, low, high):
        pivot = data[(low + high) // 2]  # Опорный — в центре
        i = low - 1
        j = high + 1

        while True:
            i += 1
            while data[i] < pivot:
                i += 1

            j -= 1
            while data[j] > pivot:
                j -= 1

            if i >= j:
                return j

            data[i], data[j] = data[j], data[i]

    if high is None:
        high = len(data) - 1

    if low < high:
        p = partition_hoare(data, low, high)
        quick_sort(data, low, p)
        quick_sort(data, p + 1, high)


def comb_sort(arr):
    """
    Comb Sort is a bubble sort with gap between elements that swaps

    :param data: data to sort inplace
    :type data: list[BasicType] or other indexable sequence[BasicType]
    """
    n = len(arr)
    shrink = 1.3
    gap = n
    is_sorted = False

    while not is_sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            is_sorted = True

        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                is_sorted = False


def trivial_sort2(data):
    """
    Sorts a container with 2 or fewer elements

    :param data: data to sort inplace
    :type data: list[BasicType] or other indexable sequence[BasicType]
    """
    if len(data) <= 1:
        pass
    if len(data) > 2:
        raise ValueError("Expected at most 2 elements!")
    if data[0] > data[1]:
        data[0], data[1] = data[1], data[0]


sorting_algs = [
    (name, obj)
    for name, obj in inspect.getmembers(sys.modules[__name__])
    if inspect.isfunction(obj) and obj.__module__ == __name__ and name.endswith("_sort")
]
