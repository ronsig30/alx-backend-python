#!/usr/bin/env python3
"""
This module contains a function to create multiple asyncio.Tasks
and return their results in ascending order.
"""

import asyncio
import importlib
from typing import List

# Dynamically import the module
tasks_module = importlib.import_module('3-tasks')
task_wait_random = tasks_module.task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay and
    returns the list of all delays in ascending order.

    Args:
        n (int): The number of times to call task_wait_random.
        max_delay (int): The maximum delay for task_wait_random.

    Returns:
        List[float]: A list of all delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
