import functools
import unittest

__all__ = [
    "given",
    "example",
    "assume",
    "reject",
    "register_random",
    "strategies",
    "HealthCheck",
    "settings",
    "Verbosity",
]

from . import strategies
from ._settings import HealthCheck, Verbosity, settings
from .control import assume, reject


def given(*_args, **_kwargs):
    def decorator(f):
        if examples := getattr(f, "_examples", []):

            @functools.wraps(f)
            def test_function(self):
                for example_args, example_kwargs in examples:
                    with self.subTest(*example_args, **example_kwargs):
                        f(self, *example_args, **example_kwargs)

        else:
            test_function = unittest.skip(
                "Hypothesis required for property test with no " +
                "specified examples"
            )(f)

        test_function._given = True
        return test_function

    return decorator


def example(*args, **kwargs):
    if bool(args) == bool(kwargs):
        raise ValueError("Must specify exactly one of *args or **kwargs")

    def decorator(f):
        base_func = getattr(f, "__wrapped__", f)
        if not hasattr(base_func, "_examples"):
            base_func._examples = []

        base_func._examples.append((args, kwargs))

        if getattr(f, "_given", False):
            # If the given decorator is below all the example decorators,
            # it would be erroneously skipped, so we need to re-wrap the new
            # base function.
            f = given()(base_func)

        return f

    return decorator


def register_random(*args, **kwargs):
    pass  # pragma: no cover
