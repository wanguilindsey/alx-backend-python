#!/usr/bin/env python3
"""Asynchronous coroutine that waits for a random delay."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay.

    Args:
        max_delay (int): The maximum number of seconds to wait. Default is 10.

    Returns:
        float: The actual number of seconds waited.
    """
    random_number = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)
    return random_number
