from numbers import Number

import pytest

from issubclass import issubclass


@pytest.mark.parametrize(
    ["obj1", "obj2", "expected"],
    [
        [1, int, False],
        [int, 1, False],
        [float, Number, True],
        [None, int, False],
        [int, None, False],
        [str, (int, float), False],
        [str, (int, float, str), True],
    ],
)
def test_all(obj1, obj2, expected: bool):
    assert issubclass(obj1, obj2) is expected
