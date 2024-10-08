#!/usr/bin/env python3
"""5. Complex types - list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ "takes a list input_list of floats and return their sum"""
    res: float = 0
    for n in input_list:
        res += n
    return res
