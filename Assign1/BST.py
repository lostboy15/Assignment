# Binary Search Tree
class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def insertNode(node,key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insertNode(node.left, key)
    else:
        node.right = insertNode(node.right, key)
    return node

def deleteNode(root,key):
    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key> root.key:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root

def minValueNode(node):
    current = node
    while ( current.left is not None):
        current = current.left
    return current

def inOrderTraversal(root):
    if root is not None:
        inOrderTraversal(root.left)

        print(str(root.key)+ '->' ,end =' ')

        inOrderTraversal(root.right)

#def preOrderTraversal(root):
   # if root is not None:
     #   preOrderTraversal(root.right)

       # print(str(root.key)+'->',end=' ')

        #preOrderTraversal(root.left)

def search(root,key):
    if root is None or root.key == key:
        return root.key

    if root.key < key:
        return search(root.right,key)
    elif root.key > key:
        return search(root.left,key)
    
root = None
root = insertNode(root,8)
root = insertNode(root,0)
root = insertNode(root,1)
root = insertNode(root,5)
root = insertNode(root,3)
root = insertNode(root,6)

inOrderTraversal(root)
print (search(root,3))

