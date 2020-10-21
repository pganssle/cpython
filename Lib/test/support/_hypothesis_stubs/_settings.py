from enum import Enum


def settings(*args, **kwargs):
    pass  # pragma: nocover


class HealthCheck(Enum):
    data_too_large = 1
    filter_too_much = 2
    too_slow = 3
    return_value = 5
    large_base_example = 7
    not_a_test_method = 8

    @classmethod
    def all(cls):
        return list(cls)


class Verbosity(Enum):
    quiet = 0
    normal = 1
    verbose = 2
    debug = 3
