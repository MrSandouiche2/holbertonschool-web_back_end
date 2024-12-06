#!/usr/bin/env python3
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Computes the sum of a list of mixed integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers and/or floats.

    Returns:
        float: The sum of all elements in the list, as a float.

    Example:
        >>> sum_mixed_list([1, 2, 3.5, 4])
        10.5
    """
    return sum(mxd_lst)
