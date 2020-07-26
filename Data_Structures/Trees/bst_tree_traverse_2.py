class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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
    
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()


if __name__ == "__main__":
    root = Node(20)
    root.insert(21)
    root.insert(19)
    root.inorder()

            

