#!/usr/bin/env python3

import random
import asyncio

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)


async def main():
    async for number in async_generator():
        print(number)

asyncio.run(main())
