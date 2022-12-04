# Write here the code challenge solution
class Node :
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class Tree:
    def __init__(self):
        self.root=None
        self.tree=''

    def print_tree(self,root):
        '''
        its a method to show the result -- just for testing --
        '''
        new_list = []
        if not root:
            new_list.append(None)
            return
        tree = [root]
        while len(tree) > 0:
            current = tree.pop(0)
            if current.left  :
                tree.append(current.left)
            if current.right :
                tree.append(current.right)
            new_list.append(current.value)
        
        return new_list

    def tree_convert_to_BST(self,node_list):
        '''
        convert to  binary search tree
        
        '''
        if len(node_list) == 0:

            return None
        elif len(node_list)==1:
            return Node(node_list[0])
        elif not node_list :
            return None
        node_list.sort()
        mid = len(node_list)//2
        root = Node(node_list[mid])
        root.left = self.tree_convert_to_BST(node_list[:mid])
        root.right = self.tree_convert_to_BST(node_list[mid+1:])
    
        return root

if __name__ == "__main__":
    tree=Tree()
    node_list= [0,-3,-10,5,9]
    root=tree.tree_convert_to_BST(node_list)
    print(tree.print_tree(root))