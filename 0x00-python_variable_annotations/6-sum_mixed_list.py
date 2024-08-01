#!/usr/bin/env python3
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of integers and floats and returns the result as a float.

    Parameters:
    mxd_lst (List[Union[int, float]]): A list containing integers and/or floats

    Returns:
    float: The sum of the elements in the list as a float.
    """
    return float(sum(mxd_lst))
