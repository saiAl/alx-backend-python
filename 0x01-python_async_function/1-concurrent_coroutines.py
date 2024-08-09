#!/usr/bin/python3
"""1. Let's execute multiple coroutines at the same time with async"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        Waits for n coroutines to finish,
            each using wait_random with max_delay.
    """
    tasks: List[float] = []

    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    completed_tasks, _ = await asyncio.wait(tasks)
    results = [await task for task in completed_tasks]
    return results
