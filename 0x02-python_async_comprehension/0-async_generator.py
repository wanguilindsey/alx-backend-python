#!/usr/bin/env python3
"""Creates an asynchronous generator."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generates random numbers.

    Each time, it asynchronously waits 1 second and then yields
    a random float between 0 and 10.

    Returns:
        Generator[float, None, None]: A generator yielding random floats.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
