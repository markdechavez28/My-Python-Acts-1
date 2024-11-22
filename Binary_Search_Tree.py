class Node:
    def __init__(self, value):
        self.value = value  
        self.left = None    
        self.right = None   

def insert(root, value):
    if root is None:
        return Node(value) 
    if value < root.value:
        root.left = insert(root.left, value) 
    else:
        root.right = insert(root.right, value) 
    return root

def search(root, value):
    if root is None or root.value == value:
        return root  
    if value < root.value:
        return search(root.left, value) 
    return search(root.right, value) 

values = [1000, 2000, 1300, 500, 1600, 1900, 1700, 650, 850, 1350, 3000, 450, 950, 1100]
root = None

for value in values:
    root = insert(root, value)

result = search(root, 1100)

if result:
    print(f"Value {result.value} found!")
else:
    print("Value not found.")







