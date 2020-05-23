class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    
    def __init__(self):
        self.head = None # for adding in front
        self.end = None # for adding at the end

    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end= "-->")
            temp = temp.next
        print()

    def traverse_reverse(self):
        temp = self.end
        while temp is not None:
            print(temp.data, end= "-->")
            temp = temp.prev
        print()
        
    def append_right(self, node):
        if self.head is None:
            self.head = node
            self.end = node
        else:
            self.end.next = node
            node.prev = self.end
            self.end = node
            
    def append_left(self, node):
        if self.head is None:
            self.head = node
            self.end = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def insert_index(self, node ,idx):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            if count == idx :
                break
            temp = temp.next

        node.next = temp.next
        temp.next = node

    def remove_left(self):
        if self.head is None:
            print("already empty")
            return -1
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            print("Removed", temp.data)
            return temp

    def remove_right(self):
        if self.end is None:
            print("Already Empty")
            return -1
        else:
            temp = self.end
            self.end = temp.prev
            print("Removed", temp.data)
            self.end.next = None
            
    def remove_node(self, val):
        temp = self.head
        while temp is not None:
            if temp.data == val:
                break
            temp = temp.next
        
        # also need to check if its first ele or last
        


if __name__ == "__main__":
    ll = LinkedList()
    ll.append_right(Node(2))
    ll.append_right(Node(3))
    ll.append_right(Node(4))
    ll.append_right(Node(5))
    ll.traverse()
    ll.traverse_reverse()
    ll.append_left(Node(9))
    ll.append_left(Node(10))
    ll.append_left(Node(11))
    ll.traverse()
    ll.traverse_reverse()
    ll.remove_left()
    ll.remove_left()
    ll.traverse()
    ll.traverse_reverse()
    ll.remove_right()
    ll.remove_right()
    ll.traverse()
    ll.traverse_reverse()
    ll.remove_node(2)