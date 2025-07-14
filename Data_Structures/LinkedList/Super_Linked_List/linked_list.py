# linked_list.py

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_head(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def insert_at_tail(self, value):
        new_node = Node(value)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
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
            new_node = Node(value)
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            new_node.next = prev.next
            prev.next = new_node
            self.size += 1

    def delete_at_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            to_delete = prev.next
            prev.next = to_delete.next
            if index == self.size - 1:
                self.tail = prev
        self.size -= 1

    def search_index(self, value):
        curr = self.head
        index = 0
        while curr:
            if curr.value == value:
                return index
            curr = curr.next
            index += 1
        return -1

    def get_length(self):
        return self.size

    def to_list(self, limit=100):
        result = []
        curr = self.head
        count = 0
        while curr and count < limit:
            result.append(curr.value)
            curr = curr.next
            count += 1
        return result

    def reverse(self):
        prev = None
        curr = self.head
        self.tail = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def has_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def find_cycle_start(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                entry = self.head
                while entry != slow:
                    entry = entry.next
                    slow = slow.next
                return entry
        return None

    def remove_cycle(self):
        start = self.find_cycle_start()
        if not start:
            return
        ptr = start
        while ptr.next != start:
            ptr = ptr.next
        ptr.next = None

    def reverse_k_group(self, head, k):
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1
        if count < k:
            return head
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head.next = self.reverse_k_group(curr, k)
        return prev

    def reverse_in_k_group(self, k):
        self.head = self.reverse_k_group(self.head, k)
        curr = self.head
        while curr and curr.next:
            curr = curr.next
        self.tail = curr

    def is_palindrome(self):
        if not self.head or not self.head.next:
            return True
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        first = self.head
        second = prev
        result = True
        while second:
            if first.value != second.value:
                result = False
                break
            first = first.next
            second = second.next
        return result

    def print_list(self, limit=100):
        """
        Prints the list in a readable format like: 1 → 2 → 3 → None
        Detects potential cycles by printing only up to `limit` nodes.
        """
        curr = self.head
        count = 0
        result = []
        while curr and count < limit:
            result.append(str(curr.value))
            curr = curr.next
            count += 1

        if curr:
            result.append("...cycle detected or limit exceeded")
        else:
            result.append("None")

        print(" → ".join(result))


if __name__ == "__main__":
    print("🔗 Singly Linked List Demo")

    ll = LinkedList()

    print("\n📌 Inserting at head and tail:")
    ll.insert_at_head(3)
    ll.insert_at_tail(5)
    ll.insert_at_head(1)
    ll.insert_at_index(2, 2)  # [1, 3, 2, 5]
    ll.insert_at_tail(6)
    ll.print_list()  # Expected: 1 → 3 → 2 → 5 → 6 → None

    print("\n📌 Deleting at index 1 (removes 3):")
    ll.delete_at_index(1)
    ll.print_list()  # Expected: 1 → 2 → 5 → 6

    print("\n📌 Searching for 5 and 42:")
    print("Index of 5:", ll.search_index(5))      # Expected: 2
    print("Index of 42:", ll.search_index(42))    # Expected: -1

    print("\n📌 Reversing the list:")
    ll.reverse()
    ll.print_list()  # Expected: 6 → 5 → 2 → 1

    print("\n📌 Checking palindrome:")
    ll2 = LinkedList()
    for val in [1, 2, 3, 2, 1]:
        ll2.insert_at_tail(val)
    ll2.print_list()
    print("Is Palindrome:", ll2.is_palindrome())  # True

    print("\n📌 Reversing in k-group (k=2):")
    ll3 = LinkedList()
    for val in [1, 2, 3, 4, 5, 6]:
        ll3.insert_at_tail(val)
    ll3.reverse_in_k_group(2)
    ll3.print_list()  # Expected: 2 → 1 → 4 → 3 → 6 → 5

    print("\n📌 Creating a cycle manually: tail → node with value 2")
    node = ll3.head
    target = None
    while node:
        if node.value == 2:
            target = node
        if node.next is None:
            node.next = target  # Create cycle
            break
        node = node.next

    print("Has Cycle:", ll3.has_cycle())  # True
    cycle_start = ll3.find_cycle_start()
    print("Cycle starts at node with value:", cycle_start.value if cycle_start else None)

    print("\n📌 Removing the cycle:")
    ll3.remove_cycle()
    print("Has Cycle:", ll3.has_cycle())  # False
    ll3.print_list()

    print("\n📌 Final List State:")
    print(f"Length: {ll3.get_length()}")
    ll3.print_list()
