# Write here the code challenge solution
class node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        if self.head is None:
            self.head = node(value)
        else:
            new_node = node(value)
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def pop(self):
        if self.head is None:
            return "is empty"
        else:
            value = self.head.value
            self.head = self.head.next
            self.size -= 1
            return value

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.value

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

class MyQueue():
    """
    this class is a queue implemented with two stacks
    """    
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, value):
        """
        push value to the queue
        """
        self.stack1.push(value)

    def pop(self):
        """
        this method pops the first element of the queue
        """        
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()
        

    def peek(self):
        """
        this method returns the first element of the queue
        """
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()

    def is_empty(self):
        """
        this method returns True if the queue is empty
        """
        return self.stack1.is_empty() and self.stack2.is_empty()

   

        
