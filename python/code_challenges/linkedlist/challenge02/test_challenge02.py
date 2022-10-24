# Write your test here
# Write your test here
import pytest
from challenge02 import *


@pytest.fixture
def linkedList1():

    linkedList1 = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    linkedList1.append(node1)
    linkedList1.append(node2)
    linkedList1.append(node3)
    linkedList1.append(node4)
    linkedList1.append(node5)

    return linkedList1.middleNode(linkedList1.head)

@pytest.fixture
def linkedList2():

    linkedList2 = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    

    linkedList2.append(node1)
    linkedList2.append(node2)
    linkedList2.append(node3)
    linkedList2.append(node4)
    linkedList2.append(node5)
    linkedList2.append(node6)
    
    return linkedList2.middleNode(linkedList2.head)



def test_Middle_node_1(linkedList1):
    actual = linkedList1
    expected =  [3,4,5]
    assert actual == expected
    
def test_Middle_node_2(linkedList2):
    actual = linkedList2
    expected = [4,5,6]
    assert actual == expected
    