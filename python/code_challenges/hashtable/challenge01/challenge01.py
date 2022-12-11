# Write here the code challenge solution

class Tree :
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None


    def __str__(self,node):
        self.print_Tree(node)
        return self.tree

    def print_Tree(self,node):
    # print the node of the tree
        if node is None:
            return None
        if node is not None:
            self.tree+=f'{node.value} ,'
        if node.left is not None:
            self.print_Tree(node.left)
        if node.right is not None:  
            self.print_Tree(node.right)


def two_sum_bst(root, k):
    """two_sum_bst is a function that takes a Binary Search tree and an integer as a parameter (k). 
    The function returns True if there are two nodes in the tree that sum up to k, otherwise it returns False.
    """
    values = set()
    def goal(root):
        if not root:
            return False
        if k - root.value in values:
            return True
        values.add(root.value)
        return goal(root.left) or goal(root.right)
    return goal(root)