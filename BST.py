from BinaryTree import treeNode
import BinaryTree

def insert(root, key): 
    if root is None: 
        return treeNode(key) 
    else: 
        if root.key == key: 
            return root 
        elif root.key < key: 
            root.right = insert(root.right, key) 
        else: 
            root.left = insert(root.left, key) 
    return root 

if __name__=="__main__":
    root=treeNode(50)
    root = insert(root, 30) 
    root = insert(root, 20) 
    root = insert(root, 40) 
    root = insert(root, 70) 
    root = insert(root, 60) 
    root = insert(root, 80)

    print("In Order: ",end=" ")
    BinaryTree.inorder(root)