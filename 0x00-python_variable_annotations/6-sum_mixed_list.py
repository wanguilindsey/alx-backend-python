#!/usr/bin/env python3
"""
Complex Types - Mixed List

This module contains a type-annotated function `sum_mixed_list` that
takes a list of integers and floats as input and returns their sum
as a float.
"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers
                                           and/or floats.

    Returns:
        float: The sum of the numbers in the list.
    """
    return sum(mxd_lst)
