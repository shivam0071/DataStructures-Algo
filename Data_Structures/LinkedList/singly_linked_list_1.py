class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None # for adding in front
        self.end = None # for adding at the end

    def travere(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end= "-->")
            temp = temp.next
        print()

    def append_right(self, node):
        if self.head is None:
            self.head = node
            self.end = node
        else:
            self.end.next = node
            self.end = node
    
    def append_left(self, node):
        if self.head is None:
            self.head = node
            self.end = node
        else:
            node.next = self.head
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
            print("Removed", temp.data)
            return temp

    def remove_right(self):
        if self.end is None:
            print("Already Empty")
            return -1
        else:
            print("DEVELOPMENT IN PROGRESS")
            
    def remove_value(self, val):
        pass




class Stack(LinkedList):

    def __init__(self):
        super().__init__()
    
    def push(self, data):
        super().append_right(Node(data))

    def pop(self):
        pass
    
# MAKING STACKS and QUEUES can be done easily now
if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    ll = LinkedList()
    ll.append_right(n1)
    ll.append_right(n2)
    ll.append_right(n3)
    ll.append_right(Node(4))
    ll.append_left(Node(9))
    ll.append_left(Node(10))
    ll.travere()
    ll.remove_left()
    ll.travere()
    ll.insert_index(Node(22), 3)
    ll.travere()
    # ll.head = n1
    # n1.next = n2
    # n2.next = n3
    

    # STACK USING LL
    s = Stack()
    s.push(33)
    s.push(44)
    s.push(55)
    print()
    s.travere()