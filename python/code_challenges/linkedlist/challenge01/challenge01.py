# Write here the code challenge solution
class Node:
    
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
#        this function to add new node 
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
  
    def printAll(self):
    
        # this function for print and return new list 
    
        list=[]
        if self.head is None :
            print("The linked list is empty")
        else :
            current = self.head
            while current is not None:
                list.append(current.value.__doc__)
                print(current.value)

                current = current.next
        print(list)
        return list

def delete_node(node):
    # this function to delete node
    if node.next is None:
        raise Exception("Can't delete the last node with this technique!")
    node.value = node.next.value
    node.next = node.next.next
    