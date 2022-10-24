from challenge01 import *
import pytest

@pytest.fixture
def linkedList2():
    ll = LinkedList()
    ll.append(4)
    ll.append(5)
    ll.append(1)
    ll.append(9)
    delete_node(ll.head.next)
    return ll.printAll()
     
    

@pytest.fixture
def linkedList3():
    ll = LinkedList()
    ll.append(4)
    ll.append(5)
    ll.append(1)
    ll.append(9)
    delete_node(ll.head.next.next)
    return ll.printAll()

def test_delete(linkedList2):
    actual = linkedList2
    expected = [4,1,9]
    assert actual == expected

def test_delete_1(linkedList3):
    actual = linkedList3
    expected =[4,5,9]
    assert actual == expected