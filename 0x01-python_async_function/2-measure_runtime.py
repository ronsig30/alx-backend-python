#!/usr/bin/env python3
"""
This module contains a function to measure the average runtime of an async coro
utine.
"""

import time
import importlib
import asyncio
from typing import List

# Dynamically import the module
concurrent_coroutines = importlib.import_module('1-concurrent_coroutines')
wait_n = concurrent_coroutines.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per call.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        float: The average time per call.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    total_time = end_time - start_time
    return total_time / n
