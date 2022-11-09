
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

    def middleNode(head_linked_list):
        if head_linked_list is None:
            return None
        else:
            mid = head_linked_list.head
            current = head_linked_list.head
            while current and current.next:
                mid = mid.next
                current = current.next.next
            return mid

    def mid_nodes(self,x):
        list_of_nodes=[]
        if self.head is None:
            return "The linked list is empty"
        else:
            current = self.head
            while current is not None:
                list_of_nodes.append(current.value)
                current = current.next
        i=list_of_nodes.index(x)
        return list_of_nodes[i:]
    def __str__(self):
        current = self.head
        output = ''
        while current:
            output += f'{{ {current.value} }} -> '
            current = current.next
        return output + 'NULL'
    def __repr__(self):
        return self.__str__()
        
        
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

    print(linkedList1)

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

    print(linkedList2)
    print(linkedList1.middleNode())