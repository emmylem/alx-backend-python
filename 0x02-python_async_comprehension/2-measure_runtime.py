#!/usr/bin/env python3
""" Comprehension project """
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start_time = asyncio.get_event_loop().time()

    """Use asyncio.gather to run async_comprehension four times in parallel."""
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)

    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time
    return total_runtime
