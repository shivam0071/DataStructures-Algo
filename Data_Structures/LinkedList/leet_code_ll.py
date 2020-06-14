import time
import collections
print("Week - \nDate 25/05/2020 - 31/05/2020")

def sweet_formatting(*deco_args):
    def normal_decorator(fun):
        def format_this(*args):
            print("Question no {}, Problem Name - {}".format(*deco_args))
            print(f"SOLUTION for INPUT - {args}")
            t1 = time.time()
            print(fun(*args))
            print(f"Time Taken {time.time() - t1} sec")
            print("*" * 20)

        return format_this
    return normal_decorator

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

    def traverse(self):
        temp = self
        while temp is not None:
            print(temp.val, end= "-->")
            temp = temp.next
        print()
    
    def __str__(self):
        temp = self
        res = []
        while temp is not None:
            res.append(temp.val)
            temp = temp.next
        return str(res)

class LinkedList:

    def __init__(self):
        self.head = None # for adding in front
        self.end = None # for adding at the end

    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end= "-->")
            temp = temp.next
        print()

    def append_right(self, node):
        if self.head is None:
            self.head = node
            self.end = node
        else:
            self.end.next = node
            self.end = node

class Solution:
    # If both lists are non-empty, I first make sure a starts smaller, use its head as result, 
    # and merge the remainders behind it. Otherwise, i.e., if one or both are empty, I just return what's there.
    
    def mergeTwoLists1(self, a, b):
        if a and b:
            if a.val > b.val:
                print(f"before If {a} --- {b}")
                a, b = b, a
                print(f"after If {a} --- {b}")
            print("Calling",a.next,b)
            a.next = self.mergeTwoLists1(a.next, b)
        # print("final A",a) 
        # print("final B",b)
        print("RETURNING", a or b)
        return a or b

    def mergeTwoLists2(self, a, b):
        # Solution 2
        # First make sure that a is the "better" one (meaning b is None or has larger/equal value). Then merge the remainders behind a.
        if not a or b and a.val > b.val:
            a, b = b, a
        if a:
            a.next  = self.mergeTwoLists2(a.next, b)
        return a
    
    # iteratively
    def mergeTwoLists3(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
        
    # recursively    
    def mergeTwoLists4(self, l1, l2):
        if not l1 or not l2:
            print("RETURNING", l1 or l2)
            return l1 or l2
        if l1.val < l2.val:
            print(f"CALLING L1 ({l1.next},{l2})")
            print(f"Current L1 {l1}")
            l1.next = self.mergeTwoLists4(l1.next, l2)
            print("L1.next is",l1.next)
            print("L1 is",l1)
            print("RETURNING L1", l1)
            return l1
        else:
            print(f"CALLING L2 ({l1},{l2.next})")
            print(f"Current L2 {l2}")
            l2.next = self.mergeTwoLists4(l1, l2.next)
            print("L2.next is",l2.next)
            print("L2 is",l2)
            print("RETURNING L2", l2)
            return l2
            
    # in-place, iteratively        
    def mergeTwoLists5(self, l1, l2):
        if None in (l1, l2):
            return l1 or l2
        dummy = cur = ListNode(0)
        dummy.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                nxt = cur.next
                cur.next = l2
                tmp = l2.next
                l2.next = nxt
                l2 = tmp
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

    def reverse_a_singly_linked_list(self, head):
        curr = head
        next = None
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        print(prev)
        return prev

    # RECURSIVE SOLUTION -
    def reverseList(self, head, prev=None):
        if not head:
          return prev
        curr, head.next = head.next, prev
        return self.reverseList(curr, head)

    # 142. Linked List Cycle II - Medium
    def detectCycle(self, head: ListNode) -> ListNode:
        # detecting loop using slow fast pointer 
        # detecting node using Floyd Cycle detection algo
        slow = head 
        fast = head
        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return self.detect_cycle_node(head, slow)
        return None
            
    def detect_cycle_node(self, head, slow):
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

        
if __name__ == "__main__":
    # 83. Remove Duplicates from Sorted List
# Runtime: 40 ms, faster than 76.58% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 13.9 MB, less than 6.45% of Python3 online submissions for Remove Duplicates from Sorted List.
    l1 = LinkedList()
    l1.append_right(Node(1))
    l1.append_right(Node(3))
    l1.append_right(Node(4))
    l2 = LinkedList()
    l2.append_right(Node(1))
    l2.append_right(Node(2))
    l2.append_right(Node(4))

    l1.traverse()
    l2.traverse()
    s = Solution()
    res = s.mergeTwoLists4(l1.head,l2.head)
    res.traverse()

    # 206. Reverse Linked List
    # Runtime: 36 ms, faster than 65.26% of Python3 online submissions for Reverse Linked List.
    # Memory Usage: 15.4 MB, less than 25.00% of Python3 online submissions for Reverse Linked List.
    print("REVERSE INPUT",l1.head)
    s.reverse_a_singly_linked_list(l1.head)

    # 23. Merge k Sorted Lists -- HARD
    # Runtime: 96 ms, faster than 94.14% of Python3 online submissions for Merge k Sorted Lists.
    # Memory Usage: 18 MB, less than 10.60% of Python3 online submissions for Merge k Sorted Lists

    # 19. Remove Nth Node From End of List -- MEDIUM
    # Runtime: 24 ms, faster than 97.40% of Python3 online submissions for Remove Nth Node From End of List.
    # Memory Usage: 14 MB, less than 6.06% of Python3 online submissions for Remove Nth Node From End of List.
