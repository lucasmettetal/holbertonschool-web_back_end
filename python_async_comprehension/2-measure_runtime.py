#!/usr/bin/env python3
"""Runtime measurement for parallel async comprehensions."""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Run async_comprehension four times in parallel and return runtime."""
    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end = time.time()
    return end - start
