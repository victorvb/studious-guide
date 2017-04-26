""" 
Author: Hyena Yu
Email: lyuvictor@gmail.com
Description: binary tree
"""


class Node():
    """ """
    def __init__(self, e=None):
        """ """
        self.data = e
        self.left = None 
        self.right = None

    def insert(self, e):
        """ insert element recursively """
        if self.data:
            if e < self.data:
                if self.left == None:
                    self.left = Node(e)
                else:
                    self.left.insert(e)
            else:
                if self.right == None :
                    self.right = Node(e)
                else:
                    self.right.insert(e)
        else:
            self.data = e

    

class Tree():
    """ """

    def __init__(self, e=None):
        """ """
        if isinstance(e, list):
            self.root = Node()
            for i in e:
                self.insert(i)
        else:
            self.root = Node(e)

    def insert(self, e):
        self.root.insert(e)

    def delete(self, e):
        pass

    def pre_order_wrapper(self):
        """ traverse the tree inorder recursively """
        self.preorder(self.root)

    def preorder(self, root):
        """ traverse the tree inorder recursively """
        if root == None:
            return False
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)

    def preorder2(self):
        """ traverse the tree inorder using stack """
        stack = []
        p = self.root
        while p != None or len(stack) != 0:
            while p != None:
                print(p.data)
                stack.append(p)
                p = p.left
            if len(stack) != 0:
                p = stack[-1]
                stack.pop()
                p = p.right

    def in_order(self):
        """ inorder wrapper function """
        self.inorder(self.root)

    def inorder(self, p):
        if p == None:
            return False

        self.inorder(p.left)
        print(p.data)
        self.inorder(p.right)

    def inorder2(self):
        """ traverse the tree using stack inorder """
        stack = []
        p = self.root
        while p != None or len(stack) != 0:
            while p != None:
                stack.append(p)
                p = p.left
            
            if len(stack) != 0:
                p = stack[-1]
                stack.pop()
                print(p.data)
                p = p.right

    def postorder(self):
        """ postorder traversal wrapper function"""
        self.post_order(self.root)

    def post_order(self, root):
        """ postorder traverse a tree recursively """
        if root == None:
            return False
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.data)
    
    def postorder2(self):
        """ postorder traverse a tree using stack
            if lastvisit is same as the right child node,
            then output the current node data
        """

        p = self.root
        first = None
        stack = []
        while p != None or len(stack) != 0:
            while p != None:
                stack.append(p)
                p = p.left

            if len(stack) != 0:
                p = stack[-1]
                if first == p.right:
                    stack.pop()
                    print(p.data)
                    p = None
                else:
                    first = p
                    p = p.right




if __name__ == '__main__':
    tree = Tree([5, 3, 2, 4, 1, 7, 6, 9, 8, 10])
    tree.postorder()
