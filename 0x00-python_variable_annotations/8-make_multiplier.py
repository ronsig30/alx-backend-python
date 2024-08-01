#!/usr/bin/env python3
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function that multiplies a given float by the multipli
    er.

    Parameters:
    multiplier (float): The multiplier to be used.

    Returns:
    Callable[[float], float]: A function that takes a float and returns the pro
    duct of that float and the multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
