#!/usr/bin/env python3
from typing import List, Tuple, Union


def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """
    Zooms into a list by repeating each element 'factor' times.

    Parameters:
    lst (List[int]): The list of integers to be zoomed.
    factor (int): The number of times each element should be repeated.

    Returns:
    List[int]: A new list with each element repeated 'factor' times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]
zoom_2x = zoom_array(array)

# Correct the type of the factor parameter to int
zoom_3x = zoom_array(array, 3)
