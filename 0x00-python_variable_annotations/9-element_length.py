#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains a sequence from the inpu
    t list and its length.

    Parameters:
    lst (Iterable[Sequence]): An iterable of sequences (e.g., lists, tuples).

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each tuple contains a se
    quence and its length.
    """
    return [(i, len(i)) for i in lst]
