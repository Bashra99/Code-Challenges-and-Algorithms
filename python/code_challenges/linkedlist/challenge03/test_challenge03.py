# Write your test here
# Write your test here
import pytest
from challenge03 import *


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

    linkedList1.Remove_nth_Node(2)
    return linkedList1.__str__()

@pytest.fixture
def linkedList2():

    linkedList2 = LinkedList()
    node1 = Node(1)

    linkedList2.append(node1)
    linkedList2.Remove_nth_Node(1)
    return linkedList2.__str__()

@pytest.fixture
def linkedList3():

    linkedList3 = LinkedList()
    node1 = Node(1)
    node2 = Node(2)

    linkedList3.append(node1)
    linkedList3.append(node2)
    linkedList3.Remove_nth_Node(1)
    return linkedList3.__str__()



def test_Remove_nth_Node_middle(linkedList1):
    actual = linkedList1
    expected ="1 --> 2 --> 3 --> 5 --> none"

    assert actual == expected
    
def test_Remove_nth_Node_one_node(linkedList2):
    actual = linkedList2
    expected = "empty linked list"
    assert actual == expected
    
def test_Remove_nth_Node_end(linkedList3):
    actual = linkedList3
    expected ='1 --> none'
    assert actual == expected