#!/usr/bin/env python3
"""
This module contains the `wait_random` coroutine that waits
for a random number of seconds between 0 and a specified maximum delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random amount of time between 0 and max_delay seconds.

    Parameters:
    max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
    float: The actual delay time in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
