#!/usr/bin/env python3
from typing import Mapping, TypeVar, Any, Union

# Define a TypeVar T for the value type in the dictionary
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) ->Union[Any, T]:
    """
    Safely get a value from a dictionary. If the key is not present, return the
    default value.

    Parameters:
    dct (Mapping): The dictionary to search in.
    key (Any): The key to look for in the dictionary.
    default (Union[T, None]): The value to return if the key is not found. Defa
    ult is None.

    Returns:
    Union[Any, T]: The value associated with the key if it exists, otherwise th
    e default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
