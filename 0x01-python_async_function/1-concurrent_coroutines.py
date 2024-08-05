#!/usr/bin/env python3
"""Execute multiple coroutines concurrently with async."""

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay
    and return a list of all the delays (float values).

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum number of seconds for delay.

    Returns:
        List[float]: List of delay times in seconds.
    """
    futures = [wait_random(max_delay) for _ in range(n)]
    futures = asyncio.as_completed(futures)
    delays = [await future for future in futures]
    return delays
