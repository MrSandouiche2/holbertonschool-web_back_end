#!/usr/bin/env python3
"""le depart"""
import random
import asyncio


async def async_generator():
    """la fonction"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
