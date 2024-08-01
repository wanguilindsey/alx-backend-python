#!/usr/bin/env python3
"""
Complex Types - List of Floats

This module contains a type-annotated function `sum_list` that takes a
list of floats as an argument and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Args:
        input_list (List[float]): A list of float numbers.

    Returns:
        float: The sum of the float numbers in the list.
    """
    return sum(input_list)
