#!/usr/bin/env python3
"""
Module to compute the floor of a given float.

This module contains the function `floor`, which takes a float as input and
returns the largest integer less than or equal to the given float.
"""

import math


def floor(n: float) -> int:
    """
    Returns the floor of a given float.

    Args:
        n (float): The float value to floor.

    Returns:
        int: The floor value of the input number.

    Example:
        >>> floor(3.14)
        3
    """
    return math.floor(n)
