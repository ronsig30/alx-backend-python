#!/usr/bin/env python3
"""
Module to measure the runtime of executing async_comprehension four times in pa
rallel.
"""

import asyncio
import time
from async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of running async_comprehension four times in par
    allel.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = time.perf_counter()
    # Execute async_comprehension four times in parallel
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
