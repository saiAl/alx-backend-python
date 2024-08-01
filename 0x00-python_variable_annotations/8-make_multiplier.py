#!/usr/bin/env python3
""" 8. Complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float multiplier as argument and
        returns a function that multiplies a float by multiplier
    """
    def multiplay(n: float) -> float:
        """ multiplay the multiplier with the number n"""
        return n * multiplier
    return multiplay
