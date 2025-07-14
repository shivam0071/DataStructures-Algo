class DLLNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_head(self, value):
        new_node = DLLNode(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_at_tail(self, value):
        new_node = DLLNode(value)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def insert_at_index(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.insert_at_head(value)
        elif index == self.size:
            self.insert_at_tail(value)
        else:
            new_node = DLLNode(value)
            curr = self.head
            for _ in range(index):
                curr = curr.next
            prev_node = curr.prev
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = curr
            curr.prev = new_node
            self.size += 1

    def delete_at_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        self.size -= 1

    def to_list_forward(self):
        curr = self.head
        result = []
        while curr:
            result.append(curr.value)
            curr = curr.next
        return result

    def to_list_backward(self):
        curr = self.tail
        result = []
        while curr:
            result.append(curr.value)
            curr = curr.prev
        return result

    def get_length(self):
        return self.size

    def print_forward(self):
        print(" → ".join(map(str, self.to_list_forward())) + " → None")

    def print_backward(self):
        print(" ← ".join(map(str, self.to_list_backward())) + " ← None")



if __name__ == "__main__":
    print("🔁 Doubly Linked List Demo")

    dll = DoublyLinkedList()

    print("\n📌 Insert at head:")
    dll.insert_at_head(30)
    dll.insert_at_head(20)
    dll.insert_at_head(10)
    dll.print_forward()     # Expected: 10 → 20 → 30 → None
    dll.print_backward()    # Expected: 30 ← 20 ← 10 ← None

    print("\n📌 Insert at tail:")
    dll.insert_at_tail(40)
    dll.insert_at_tail(50)
    dll.print_forward()     # Expected: 10 → 20 → 30 → 40 → 50 → None
    dll.print_backward()    # Expected: 50 ← 40 ← 30 ← 20 ← 10 ← None

    print("\n📌 Insert at index (2 → insert 25):")
    dll.insert_at_index(2, 25)
    dll.print_forward()     # Expected: 10 → 20 → 25 → 30 → 40 → 50 → None

    print("\n📌 Delete at index (4 → delete 40):")
    dll.delete_at_index(4)
    dll.print_forward()     # Expected: 10 → 20 → 25 → 30 → 50 → None
    dll.print_backward()    # Expected: 50 ← 30 ← 25 ← 20 ← 10 ← None

    print("\n📌 Insert at index 0 (head) → 5:")
    dll.insert_at_index(0, 5)
    dll.print_forward()     # Expected: 5 → 10 → ...

    print("\n📌 Delete tail (last index):")
    dll.delete_at_index(dll.get_length() - 1)
    dll.print_forward()     # Last element (50) removed

    print("\n📌 Final State:")
    print(f"Length: {dll.get_length()}")
    dll.print_forward()
    dll.print_backward()
