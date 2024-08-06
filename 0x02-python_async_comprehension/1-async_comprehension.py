#!/usr/bin/env python3
"""
This module contains a coroutine that uses async comprehension to collect valus
from an async generator.
"""

from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers from the async_generator using async comprehensio
    n.

    Returns:
        A list of 10 random float numbers.
    """
    return [num async for num in async_generator()]
