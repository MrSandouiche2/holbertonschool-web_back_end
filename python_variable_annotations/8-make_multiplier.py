#!/usr/bin/env python3
"""
Module that defines a function `make_multiplier` which returns a function
that multiplies a number by a given multiplier.

The `make_multiplier` function takes a float multiplier as an argument
and returns a function that multiplies its argument by this multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given number by the multiplier.

    Args:
        multiplier (float): The multiplier to be used in the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the result of multiplying it by `multiplier`.
    """
    def multiplier_function(n: float) -> float:
        """Returns the product of n and the multiplier."""
        return n * multiplier

    return multiplier_function
