#!/usr/bin/env python3
"""6. Complex types - mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Takes list of integer and returns their sum as float"""
    res: int = 0
    for n in mxd_lst:
        res += n
    return float(res)
