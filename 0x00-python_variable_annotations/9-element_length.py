#!/usr/bin/env python3
"""9. Let's duck type an iterable object"""
from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return the element length"""
    return [(i, len(i)) for i in lst]