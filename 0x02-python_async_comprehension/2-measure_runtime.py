#!/usr/bin/env python3
"""Measures the total runtime of executing async functions."""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel and measures the
    total runtime.

    Returns:
        float: The total time taken to execute the four
        async_comprehension calls.
    """
    start_time = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    return time.perf_counter() - start_time
