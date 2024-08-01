#!/usr/bin/env python3
"""
Duck Typing - First Element of a Sequence

Augment code with correct duck-typed annotations.
"""

from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of a sequence if it exists.

    Args:
        lst (Sequence[Any]): A sequence (e.g., list, tuple) of any type.

    Returns:
        Union[Any, None]: The first element of the sequence if it exists,
                           otherwise None.
    """
    if lst:
        return lst[0]
    return None
