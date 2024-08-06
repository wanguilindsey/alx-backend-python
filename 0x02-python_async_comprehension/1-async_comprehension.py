#!/usr/bin/env python3
"""Generates a list from an async comprehension."""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects a list of floats from async_generator.

    Returns:
        List[float]: A list of floats generated asynchronously.
    """
    return [item async for item in async_generator()]
