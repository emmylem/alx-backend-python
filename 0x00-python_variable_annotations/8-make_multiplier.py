#!/usr/bin/python3
"""Typing Python Project."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a Callable Function."""
    def a(n: float) -> float:
        return n * multiplier
    return a
