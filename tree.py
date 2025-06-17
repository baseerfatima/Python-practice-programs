class trees:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insert(self,value):
        if value<self.data:
            if self.left is None:
                self.left=trees(value)
            else:
                self.left.insert(self,value)
        else:
            if self.right is None:
                self.right=trees(value)
            else:
                self.right.insert(self,value)
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
root=trees(10)
root.insert(8)
root.insert(11)
root.inorder(root)