class Node :
    def __init__(self, key) -> None:
        self.key = key 
        self.left = None
        self.right = None



        # 50
       # /  \
      # 50    50
     # /  \   /  \
   # 20   70 60   80      
        
def search(root, key):

    if root is None or root.key == key:
        return root

    if root.key < key:
        return search(root.right, key)
    return search(root.left, key)



root= Node(50)

root.left = Node(50)

root.right = Node(50)

root.left.left = Node(20)

root.left.right = Node(70)

root.right.left = Node(60)

root.right.right = Node(80)


print("Found" if search(root, 10) else "Not Found")
print("Found" if search(root, 80) else "Not Found")