#!/usr/bin/env python3
"""
The modle contains the `wait_n` coroutine tht spawns multiples of `wait_random`
and returns their results in ascending order.
"""

import asyncio
from heapq import heappush, heappop
from typing import List
from _basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `wait_random` coroutine `n` times with the specified `max_delay`,
    the list of all delays in ascending order.

    Parameters:
    n (int): The number of coroutines to spawn.
    max_delay (int): The maximum delay for each coroutine.

    Returns:
    List[float]: The list of delays sorted in ascending order.
    """
    delays = []
    heap = []

    async def task_wrapper():
        delay = await wait_random(max_delay)
        heappush(heap, delay)
    tasks = [task_wrapper() for _ in range(n)]
    await asyncio.gather(*tasks)

    while heap:
        delays.append(heappop(heap))

    return delays
