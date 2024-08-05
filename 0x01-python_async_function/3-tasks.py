#!/usr/bin/env python3
"""Create an asyncio task."""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio task for wait_random with the given max_delay.

    Args:
        max_delay (int): The maximum number of seconds for delay.

    Returns:
        asyncio.Task: A task object for the coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
