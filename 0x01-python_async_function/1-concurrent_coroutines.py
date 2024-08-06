#!/usr/bin/env python3
"""
This module contains a coroutine that spawns multiple instances
of an asynchronous task and returns their results in ascending order.
"""

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    and returns the list of delays in ascending order.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: A list of delay times in ascending order.
    """
    delays = []
    # Use asyncio.gather to run multiple coroutines concurrently
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))

    completed_delays = []
    for delay in asyncio.as_completed(delays):
        completed_delays.append(await delay)

    return completed_delays
