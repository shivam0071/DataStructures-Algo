
# 83. Remove Duplicates from Sorted List
# Runtime: 40 ms, faster than 76.58% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 13.9 MB, less than 6.45% of Python3 online submissions for Remove Duplicates from Sorted List.

If both lists are non-empty, I first make sure a starts smaller, use its head as result, and merge the remainders behind it. Otherwise, i.e., if one or both are empty, I just return what's there.

class Solution:
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b

    def mergeTwoLists2(self, a, b):
        # Solution 2
        # First make sure that a is the "better" one (meaning b is None or has larger/equal value). Then merge the remainders behind a.
        if not a or b and a.val > b.val:
            a, b = b, a
        if a:
            a.next  = self.mergeTwoLists(a.next, b)
        return a
    
    # iteratively
    def mergeTwoLists1(self, l1, l2):
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
    def mergeTwoLists2(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
            
    # in-place, iteratively        
    def mergeTwoLists(self, l1, l2):
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

