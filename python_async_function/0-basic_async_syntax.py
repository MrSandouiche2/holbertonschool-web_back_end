#!/usr/bin/env python3
"""
Asynchronous coroutine that waits for a random delay between 0 and max_delay.

This coroutine takes an integer max_delay (defaulting to 10), waits for random
amount of time between 0 and max_delay (inclusive), and returns the delay
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay between 0 and max_delay.

    Args:
        max_delay (int): The maximum delay in seconds (default is 10).

    Returns:
        float: The random delay that was waited for, in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
