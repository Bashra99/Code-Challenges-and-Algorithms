# Write your test here
# Write your test here
import pytest
from challenge02 import *

def test_find_middle_node():
    linkedList1 = LinkedList()
    for i in [1,2,3,4,5]:
        node = Node(i)
        linkedList1.append(node)
    assert linkedList1.middleNode() == 3  
    assert linkedList1.mid_nodes(3) == [3,4,5]  

def test_find_middle_node2():
    linkedList2 = LinkedList()
    for i in [1,2,3,4,5,6]:
        node = Node(i)
        linkedList2.append(node)
    assert linkedList2.middleNode() == 4
    assert linkedList2.mid_nodes(4) == [4,5,6]