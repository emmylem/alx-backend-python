#!/usr/bin/env python3
"""Comprehension Project."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Coroutine will loop 10 Times."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
