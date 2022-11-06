# Write your test here
import pytest
from challenge01 import *


def test_one():
    tree = Tree()
    return tree.pre_in_order([3,9,20,15,7],[9,3,15,20,7])
    actual =tree
    expected=[3,9,20,None,None,15,7]
    assert actual==expected

def test_three():
    tree = Tree()
    return tree.pre_in_order([-1], [-1])
    actual =tree
    expected=[-1]
    assert actual==expected
