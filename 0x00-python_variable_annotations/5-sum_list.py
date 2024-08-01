#!/usr/bin/env python3
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of floats and returns the result as a float.

    Parameters:
    input_list (List[float]): A list of floats to sum.

    Returns:
    float: The sum of the elements in the list as a float.
    """
    return float(sum(input_list))
