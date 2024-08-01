#!/usr/bin/env python3
"""
Type Checking

Use mypy to validate the code and apply any necessary changes.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zoom in on the given tuple by repeating each element.

    Args:
        lst (Tuple[int, ...]): A tuple of integers.
        factor (int): The number of times to repeat each element.

    Returns:
        List[int]: A list where each element from the tuple is repeated
                   `factor` times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array: Tuple[int, ...] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
