#!/usr/bin/env python3
from typing import Callable
"""fonction"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_function(n: float) -> float:
        """Returns:
            float"""
        return n * multiplier
    """Return:"""
    return multiplier_function
