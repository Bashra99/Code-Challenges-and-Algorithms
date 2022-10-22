from challenge01 import *
import pytest

@pytest.fixture
def linkedList1():
    linkedList1 = LinkedList()
    linkedList1.append(4)
    linkedList1.append(5)
    linkedList1.append(1)
    linkedList1.append(9)
    linkedList1.delete_node(5)
    x=linkedList1.printAll()

    return x
@pytest.fixture
    
def linkedList2():
    linkedList2 = LinkedList()
    linkedList2.append(4)
    linkedList2.append(5)
    linkedList2.append(1)
    linkedList2.append(9)
    linkedList2.delete_node(1)
    x=linkedList2.printAll()
    return x

def test_delete(linkedList1):
    actual = linkedList1
    expected = [4,1,9]
    assert actual == expected

def test_delete_1(linkedList2):
    actual = linkedList2
    expected =[4,5,9]
    assert actual == expected