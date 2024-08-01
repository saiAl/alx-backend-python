#!/usr/bin/env python3
""" 7. Complex types - string and int/float to tuple """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ that takes a string k and an int OR float v
        as arguments and returns a tuple.
    """
    return (k, v**2)
