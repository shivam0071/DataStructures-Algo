class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:    
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def find(self, data):
        if data < self.data:
            if self.left is None:
                return False
            return self.left.find(data)
        elif data > self.data:
            if self.right is None:
                return False
            return self.right.find(data)
        else:
            return True
        
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()


root = Node(10)
root.insert(6)
root.insert(3)
root.insert(14)
root.insert(24)
root.insert(44)
root.insert(5)
root.insert(2)
root.insert(4)

#      (10)
#      /   \
#     6     14
#    /        \
#    3          24
#   / \            \
#  2   5            44
#      /
#     4

root.PrintTree()
# 2, 3, 4, 5, 6, 10, 14, 24, 44
print("END", root.data, root.left.data, root.right.data)
print(root.find(44))
