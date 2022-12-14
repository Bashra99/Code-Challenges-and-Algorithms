# Write your test here
import pytest
from challenge03 import *

@pytest.fixture
def tree1():
    tree1=Tree()
    node_list= [0,-3,-10,5,9]
    root=tree1.tree_convert_to_BST(node_list)
    return tree1.print_tree(root)

@pytest.fixture
def tree2():
    tree2=Tree()
    node_list=  [1,3]
    root=tree2.tree_convert_to_BST(node_list)
    return tree2.print_tree(root)


def test_tree_convert_to_BST_tree1(tree1):
    actual = tree1
    expected = [0, -3, 9, -10, 5]
    assert actual == expected
    


def test_tree_convert_to_BST_tree2(tree2):
    actual = tree2
    expected = [3, 1]
    assert actual == expected

@pytest.fixture
def tree3():
    tree3 = Tree()
    node_list=[]
    root=tree3.tree_convert_to_BST(node_list)
    return tree3.print_tree(root)
def test_four_convert_to_BST_tree3(tree3):
    actual = tree3
    expected = None
    assert actual == expected

@pytest.fixture
def tree4():
    tree4 = Tree()
    node_list=[1]
    root=tree4.tree_convert_to_BST(node_list)
    return tree4.print_tree(root)

def test_five_convert_to_BST_tree4(tree4):
    actual = tree4
    expected = [1]
    assert actual == expected
