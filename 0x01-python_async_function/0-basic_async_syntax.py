#!/usr/bin/env python3
""" 0. The basics of async """
import asyncio
import random
import typing

async def wait_random(max_delay: int =10) -> float:
    """ asynchronous coroutine """
    return random.uniform(0, max_delay)
 

