#!/usr/bin/python3
"""Typing Python Project."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """A union of Int or Float."""
    return k, v ** 2
