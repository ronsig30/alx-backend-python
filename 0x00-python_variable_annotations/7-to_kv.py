#!/usr/bin/env python3
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a key-value pair to a tuple where the key is a string and the valu
    e is the square of the given number.

    Parameters:
    k (str): The key as a string.
    v (Union[int, float]): The value, which can be an int or a float.

    Returns:
    Tuple[str, float]: A tuple where the first element is the key and the secon
    d element is the square of the value.
    """
    return (k, float(v ** 2))
