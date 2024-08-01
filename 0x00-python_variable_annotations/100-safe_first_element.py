#!/usr/bin/env python3
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely returns the first element of a sequence if it exists; otherwise, ret
    urns None.

    Parameters:
    lst (Sequence[Any]): The input sequence from which to retrieve the first el
    ement.

    Returns:
    Union[Any, None]: The first element of the sequence if it exists; otherwise
    , None.
    """
    if lst:
        return lst[0]
    else:
        return None
