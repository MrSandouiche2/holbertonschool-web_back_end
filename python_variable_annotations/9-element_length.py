#!/usr/bin/env python3
"""fonction"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return"""
    return [(i, len(i)) for i in lst]
