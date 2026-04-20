"""
Counting container and value
"""

from __future__ import annotations
from typing import Generic, TypeVar, Optional
from functools import total_ordering
from beartype import beartype

T = TypeVar("T")


@beartype
class CountingList(Generic[T]):
    """
    A wrapper around a Python list that acts like an array and counts assignments
    """

    _assignments: int = 0

    @classmethod
    def assignments(cls) -> int:
        """
        Return the total number of assignments

        :return: Total number of assignments
        :rtype: int
        """
        return cls._assignments

    @classmethod
    def likely_swaps(cls) -> int:
        """
        Return an approximate number of swaps assuming one swap ~ two assignments

        :return: Estimated number of swaps (integer division)
        :rtype: int
        """
        return cls._assignments // 2

    @classmethod
    def reset_stats(cls) -> None:
        """
        Reset stats to zero
        """
        cls._assignments = 0

    def __init__(self, data: Optional[list[T]] = None):
        """
        Initialize the container, optionally with a list

        :param data: Optional initial data
        :type data: list[BasicType] or None
        """
        self._array: list[T] = list(data) if data is not None else []

    def __getitem__(self, index: int) -> T:
        """
        Get the element at the given index

        :param int index: Index of the element
        :return: The value at the specified index
        :rtype: BasicType
        :raises IndexError: If index is out of range (same behaviour as list.__getitem__)
        """
        return self._array[index]

    def __setitem__(self, index: int, value: T) -> None:
        """
        Set the element at the given index and increment the assignment counter

        :param int index: Index to set
        :param value: Value to write
        :type value: BasicType
        :raises IndexError: If index is out of range (same behaviour as list.__setitem__)
        """
        type(self)._assignments += 1
        self._array[index] = value

    def __len__(self) -> int:
        """
        Return the number of elements in the container

        :return: Length of the container
        :rtype: int
        """
        return len(self._array)

    def __repr__(self) -> str:
        """
        Return a representation of the container for debugging

        :return: Representation string
        :rtype: str
        """
        return f"CountingContainer({self._array!r})"


@beartype
@total_ordering
class CountingOrdered(Generic[T]):
    """
    A wrapper for values that counts comparisons
    """

    _comparisons: int = 0

    @classmethod
    def comparisons(cls) -> int:
        """
        Total number of comparisons

        :return: Total comparisons count
        :rtype: int
        """
        return cls._comparisons

    @classmethod
    def reset_stats(cls) -> None:
        """
        Reset the comparisons counter to zero
        """
        cls._comparisons = 0

    def __init__(self, value: T):
        """
        Initialize a comparable wrapper for a value

        :param value: The underlying value to compare.
        :type value: BasicType
        """
        self._value = value

    def __eq__(self, other: object) -> bool:
        """
        Equality comparison that increments the comparisons counter

        :param other: The object to compare with.
        :type other: object
        :return: True if values are equal, False otherwise
        :rtype: bool
        :raises TypeError: If `other` is not a CountingOrdered
            instance (returns NotImplemented
            to allow reflected operations).
        """
        if not isinstance(other, CountingOrdered):
            return NotImplemented
        type(self)._comparisons += 1
        return self._value == other._value

    def __lt__(self, other: object) -> bool:
        """
        Less-than comparison that increments the comparisons counter

        :param other: The object to compare with
        :type other: object
        :return: True if self < other, False otherwise
        :rtype: bool
        :raises TypeError: If `other` is not a CountingOrdered instance (returns NotImplemented
            to allow reflected operations).
        """
        if not isinstance(other, CountingOrdered):
            return NotImplemented
        type(self)._comparisons += 1
        return self._value < other._value

    def __gt__(self, other: object) -> bool:
        """
        Greater-than comparison that increments the comparisons counter

        :param other: The object to compare with
        :type other: object
        :return: True if self > other, False otherwise
        :rtype: bool
        :raises TypeError: If `other` is not a CountingOrdered instance (returns NotImplemented
            to allow reflected operations).
        """
        if not isinstance(other, CountingOrdered):
            return NotImplemented
        type(self)._comparisons += 1
        return self._value > other._value

    def __repr__(self) -> str:
        """
        Return a representation of the comparable wrapper for debugging.

        :return: Representation string.
        :rtype: str
        """
        return f"CountingOrdered({self._value!r})"
