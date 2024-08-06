#!/usr/bin/env python3
"""
This module contains a function to create an asyncio.Task
from a coroutine.
"""

import asyncio
import importlib

# Dynamically import the module
basic_async_syntax = importlib.import_module('0-basic_async_syntax')
wait_random = basic_async_syntax.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: The task object for the coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
