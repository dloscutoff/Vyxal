"""
This file is for testing specific elements that can't go in elements.yaml
"""

import os
import sys
import sympy

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__)) + "/.."
sys.path.insert(1, THIS_FOLDER)

from vyxal.transpile import *
from vyxal.elements import *
from vyxal.context import Context
from vyxal.helpers import *
from vyxal.LazyList import *


def run_vyxal(vy_code, inputs=[], *, debug=False):
    stack = list(map(vyxalify, inputs))
    ctx = Context()
    ctx.stacks.append(stack)

    py_code = transpile(vy_code)
    if debug:
        print(py_code)
    exec(py_code)

    ctx.stacks.pop()
    return stack


def test_vertical_mirror():
    """Test øṁ"""
    # Join these on newlines into one string and check if the result
    # is as expected
    tests = [
        ("abc", "abccba"),
        ("aj38asd#f|", "aj38asd#f||f#dsa83ja"),
        ("ಠ_ಠ¯\\_(ツ)_/¯", "ಠ_ಠ¯\\_(ツ)_/¯¯/_)ツ(_\\¯ಠ_ಠ"),
        ("><>", "><>><>"),
    ]

    input_str = "\n".join(test[0] for test in tests)
    expected = "\n".join(test[1] for test in tests)

    stack = run_vyxal("øṁ", [input_str])

    actual = stack[-1]
    assert actual == expected


def test_sort_by():
    """Test µ"""

    stack = run_vyxal("314 µ;", [])
    assert stack[-1] == [1, 3, 4]

    stack = run_vyxal("59104 µ;", [])
    assert stack[-1] == [0, 1, 4, 5, 9]


def test_cumulative_reduce():
    """Test ɖ"""

    stack = run_vyxal("12345 ɖ+")
    assert stack[-1] == [1, 3, 6, 10, 15]

    stack = run_vyxal("34212 ɖ-")
    assert stack[-1] == [3, -1, -3, -4, -6]


def test_map_lambda_as_element():
    """Test that a map lambda is held as a single element"""
    stack = run_vyxal("⁽ƛ1+;M", inputs=[[[1, 2], [3, 4]]])
    assert stack[-1] == [[2, 3], [4, 5]]


def test_vectorise_map_lambda():
    """Test that a map lambda can be vectorised"""
    stack = run_vyxal("vƛ30∴;", inputs=[[[34, 1324, 23], [45, 3]]])
    assert simplify(stack[-1]) == [[34, 1324, 30], [45, 30]]


def test_deep_flatten_inf_list():
    """Test that an infinite list can be fully flattened"""
    stack = run_vyxal("⁽› 1 5 r w Ḟ f")
    assert simplify(stack[:10][0][:10]) == [1, 2, 3, 4, 2, 3, 4, 5, 3, 4]


def test_overdot_X_function_overload():
    stack = run_vyxal("4λ2ḭ;Ẋ")
    assert stack[-1] == 0
