#!/usr/bin/env python3
"""docstring"""
from typing import Union, Tuple
"""fonction"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return: va return"""
    return (k, float(v ** 2))
