#!/usr/bin/python3
"""Typing Python Project."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum of List of Int or Float."""
    return sum(mxd_lst)
