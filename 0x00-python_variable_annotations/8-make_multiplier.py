#!/usr/bin/env python3
"""
Complex Types - Functions

This module contains a type-annotated function `make_multiplier` that
takes a float multiplier as an argument and returns a function that
multiplies a float by the given multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.

    Args:
        multiplier (float): The multiplier to be used.

    Returns:
        Callable[[float], float]: A function that multiplies its input
                                   by the given multiplier.
    """
    def fn(num: float) -> float:
        return num * multiplier

    return fn
