
# Write here the code challenge solution
class Node:
    
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
            #append method take a node and put it in the Linked List

        if not self.head:
            self.head = value
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = value

    def middleNode(self, head):
      # this method to return  the middle node

        mid_node = []
        while head is not None:
            mid_node.append(head.value)
            head = head.next
        return mid_node[len(mid_node)//2:]
        
if __name__ == "__main__":
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

    print(linkedList1.middleNode(linkedList1.head))

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

    print(linkedList2.middleNode(linkedList2.head))