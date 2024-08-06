#!/usr/bin/env python3
"""
This module contains a coroutine to measure the runtime of executing
async_comprehension four times in parallel.
"""

import asyncio
import time
from typing import Callable

# Import async_comprehension from the previous file
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of executing async_comprehension four times in parallel

    Returns:
        The total runtime in seconds.
    """
    start_time = time.time()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()
    return end_time - start_time
