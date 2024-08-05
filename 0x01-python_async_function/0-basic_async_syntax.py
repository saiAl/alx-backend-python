#!/usr/bin/env python3
""" 0. The basics of async """
import asyncio
import random


async def wait_random(max_delay=10):
    """ asynchronous coroutine """
    return random.uniform(0, max_delay)

