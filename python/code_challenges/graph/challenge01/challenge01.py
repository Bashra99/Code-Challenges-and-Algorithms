# Write here the code challenge solution
class Node:
    def __init__(self, value=None):
        self.value = value
    
    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

class Edge:
    def __init__(self,vertex,weight=0):
        self.vertex = vertex
        self.weight = weight

    def __str__(self):
        return f'{self.vertex}'


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, value):
        node = Node(value)

        if not self.rear: # if the queue empty
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):

        if self.front == None:
            return("This queue is empty")        
        if self.front == self.rear:
            self.rear = None
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

    def is_empty(self):
        if self.front == None:
            return True
        return False

    def peek(self):
        if self.front == None:
            return("This queue is empty")        
        return self.front.value

    def __str__(self):
        output = ''
        current = self.front
        while current:
            output += f'{{ {current.value} }} -> '
            current = current.next
        output += 'None'
        return output
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self,value):
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        return new_vertex

    def add_edge(self,node1,node2,weight=0):
        if not node1 in self.adj_list.keys():
            return("this node does not exist")
        if not node2 in self.adj_list.keys():
            return("this node does not exist") 
        edge1 = Edge(node2,weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1,weight)
        self.adj_list[node2].append(edge2)

    def __str__(self):
        output = ''
        for vertex in self.adj_list.keys():
            output+= f'{vertex} ->'
            for edge in self.adj_list[vertex]:
                output+= f'{edge.vertex} ---> '
            output+= '\n'
        return output

    def breadth_first_traversal(self, start_value):
        """
        breadth_first_traversal is a method that take a value as a parameter;and return a list of all the nodes in the graph in the order they were visited.
        """
        visited = []
        queue = [start_value]
        while queue:
            current_node = queue.pop(0)
            if current_node not in visited:
                visited.append(current_node)
                for edge in self.adj_list[current_node]:
                    queue.append(edge.vertex)
        return visited

if __name__ == "__main__":
    graph = Graph()
    a = graph.add_node('a')
    c = graph.add_node('c')
    b = graph.add_node('b')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    g = graph.add_node('g')
    h = graph.add_node("h")
    i = graph.add_node("i")
    k = graph.add_node("k")

    graph.add_edge( a,  c)
    graph.add_edge( a,  e)
    graph.add_edge( a,  b)
    graph.add_edge( c,  f)
    graph.add_edge( b,  d)
    graph.add_edge( e,  g)
    graph.add_edge( e,  d)
    graph.add_edge( e,  f)
    graph.add_edge( f,  i)
    graph.add_edge( f,  h)
    graph.add_edge( g, h)
    graph.add_edge( h, k)
    graph.add_edge( i, k)
    print(graph)
    print(graph.breadth_first_traversal(a))
           
