# Write here the code challenge solution
class Node:
    #Node class to make a node and it take a value for the node
    def __init__(self,vlaue):
        self.next = None
        self.value = vlaue



class Stack:
    #Stack class have method for push, pop, peek,empty

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,value):
    #push method take a node and put it in the Stack
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
    # pop function is a function that take the node and delete it from the Stack

        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
            return("This is empty")
    
    def peek(self):
    #peek method value for node and get it 

        if self.top:
            return self.top.value
        else:
            return("This is empty")

    def get_size(self):
    # return the size of the stack
        return self.size

def is_Valid(s):
    Brackets={'(':')','{':'}','[':']'}
    stack=Stack()
    for i in s:
        if i in Brackets.keys():
            stack.push(i)

        else:
            if i in Brackets.values():
                if stack.get_size() !=0:
                    Open_Bracket=stack.pop()
                else:
                    return False        
                if i != Brackets[Open_Bracket]:
                    return False        
    return True 