# Write here the code challenge solution
class Node:
    
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        # printAll method print and return new list 
        # and if the linked list is empty it return empty linked list
        output=""
        if self.head is None :
            output= "empty linked list"
        else :
            current = self.head
            while current :
                output+=f'{current.value} --> '
                current=current.next
            output+='none'
        return output

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
      
    
    def Remove_nth_Node(self,n):
        '''Remove_nth_Node method it take n as a parameter and remove the node from the end of the linked list'''
        slow=self.head
        fast=self.head
        for i in range(n):
            fast=fast.next
        if fast is None:
            self.head = self.head.next
            return self.head
        while fast.next :
            fast = fast.next
            slow = slow.next   
        slow.next = slow.next.next
        return self.head

def delete(node):
    nextNode = node.next
    node.value = nextNode.value
    node.next = nextNode.next