class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def inorder_traversal(root, result):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.val)
        inorder_traversal(root.right, result)

def tree_sort(arr):
    root = None
    for item in arr:
        root = insert(root, item)
    
    result = []
    inorder_traversal(root, result)
    return result

# Ejemplo de uso:
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista desordenada:", lista)
sorted_list = tree_sort(lista)
print("Lista ordenada:   ", sorted_list)