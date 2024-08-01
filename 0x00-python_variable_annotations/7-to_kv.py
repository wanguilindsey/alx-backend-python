#!/usr/bin/env python3
"""
Complex Types - String and Int/Float to Tuple

This module contains a type-annotated function `to_kv` that takes a
string and an integer or float, and returns a tuple where the first
element is the string and the second element is the square of the
numeric value.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple from a string and the square of a number.

    Args:
        k (str): The string value.
        v (Union[int, float]): The integer or float to be squared.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string
                           and the second element is the square of v.
    """
    return (k, v * v)
