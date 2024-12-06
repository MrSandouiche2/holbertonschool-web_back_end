#!/usr/bin/env python3
"""
fonction
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `n` tasks that call `wait_random` and waits for their completion.

    """
    tasks = []
    delays_of_tasks = []
    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays_of_tasks.append(delay)
    return delays_of_tasks
