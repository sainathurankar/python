class treeNode:
    def __init__(self):
        self.key=0
        self.left=None
        self.right=None
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def preorder(root):
    if root:
        print(root.key,end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key,end=" ")
                                                            #Tree Structure
if __name__=="__main__":                                        #1
    root=treeNode(1)                                       #2         3
    root.left=treeNode(2)                              #4       5  6     7
    root.right=treeNode(3)
    root.left.left=treeNode(4)
    root.left.right=treeNode(5)
    root.right.left=treeNode(6)
    root.right.right=treeNode(7)


    print("Pre Order: ", end=" ")
    preorder(root)
    print("\nIn Order: ", end=" ")
    inorder(root)
    print("\nPost Order: ", end=" ")
    postorder(root)



