# Write here the code challenge solution
class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
           
    def pre_oreder(root):
        if root is None:
            return
        print(root.value)
        pre_oreder(root.left)
        pre_oreder(root.right)

    def in_order(root):
        if root is None:
            return
        in_order(root.left)
        print(root.value)
        in_order(root.right)

    def post_order(root):
        if root is None:
            return
        post_order(root.left)
        post_order(root.right)
        print(root.value)

    def pre_in_order(self,preorder,inorder):
        """
         A function that takes two lists preorder and inorder as arguments and return a root 
        """        

        if not preorder or not inorder or not len(preorder)==len(inorder):
            return None
        
        root = node(preorder[0])
        root_index = inorder.index(root.value)
        root.left = self.pre_in_order(preorder[1:root_index+1],inorder[:root_index])
        root.right = self.pre_in_order(preorder[root_index+1:],inorder[root_index+1:])
        return root




