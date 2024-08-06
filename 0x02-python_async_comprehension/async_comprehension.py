#!/usr/bin/env python3
"""
Module to demonstrate asynchronous list comprehension over an async generator.
"""

from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously collects 10 random numbers from async_generator using async 
    comprehension.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    return [number async for number in async_generator()]
