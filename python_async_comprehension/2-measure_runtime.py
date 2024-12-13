#!/usr/bin/env python3
"""temps d'exec"""
import asyncio
import time
from typing import Callable
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Mesure le temps total """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
