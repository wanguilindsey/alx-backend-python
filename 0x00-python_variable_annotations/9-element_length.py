#!/usr/bin/env python3
"""
Duck Type Iterable Object

Annotate a function parameter and return values with appropriate types.
"""

from typing import Sequence, Iterable, List, Tuple


def element_length(
    lst: Iterable[Sequence]
) -> List[Tuple[Sequence, int]]:
    """
    Create a list of tuples with each sequence and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences
                                   (e.g., lists, strings).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple
                                     contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
