#!/usr/bin/env python3
"""fonction"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """calcule le début et la fin de l'index"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
