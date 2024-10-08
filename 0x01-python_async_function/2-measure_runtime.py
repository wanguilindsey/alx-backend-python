#!/usr/bin/env python3
"""Measures the total execution time for wait_n(n, max_delay)."""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time for wait_n(n, max_delay).

    Args:
        n (int): The number of times wait_n is called.
        max_delay (int): The maximum number of seconds for delay.

    Returns:
        float: The average time per wait_n call.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    return (end_time - start_time) / n
