import unittest

__all__ = [
    "reject",
    "assume",
]


def assume(condition):
    if not condition:
        raise unittest.SkipTest("Unsatisfied assumption")
    return True


def reject():
    assume(False)
