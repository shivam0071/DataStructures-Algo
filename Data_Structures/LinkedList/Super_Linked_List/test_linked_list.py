# test_linked_list.py

import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()
        for value in [1, 2, 3, 4, 5]:
            self.ll.insert_at_tail(value)

    def test_insert_head_tail(self):
        self.ll.insert_at_head(0)
        self.ll.insert_at_tail(6)
        self.assertEqual(self.ll.to_list(), [0, 1, 2, 3, 4, 5, 6])

    def test_insert_delete_at_index(self):
        self.ll.insert_at_index(3, 99)
        self.assertEqual(self.ll.to_list(), [1, 2, 3, 99, 4, 5])
        self.ll.delete_at_index(3)
        self.assertEqual(self.ll.to_list(), [1, 2, 3, 4, 5])

    def test_search(self):
        self.assertEqual(self.ll.search_index(3), 2)
        self.assertEqual(self.ll.search_index(100), -1)

    def test_reverse(self):
        self.ll.reverse()
        self.assertEqual(self.ll.to_list(), [5, 4, 3, 2, 1])

    def test_reverse_k_group(self):
        self.ll.reverse_in_k_group(2)
        self.assertEqual(self.ll.to_list(), [2, 1, 4, 3, 5])

    def test_is_palindrome(self):
        pal_ll = LinkedList()
        for val in [1, 2, 3, 2, 1]:
            pal_ll.insert_at_tail(val)
        self.assertTrue(pal_ll.is_palindrome())
        pal_ll.insert_at_tail(0)
        self.assertFalse(pal_ll.is_palindrome())

    def test_cycle_detection_and_removal(self):
        # Manually create cycle: tail -> head.next (node 2)
        tail = self.ll.tail
        tail.next = self.ll.head.next
        self.assertTrue(self.ll.has_cycle())
        start = self.ll.find_cycle_start()
        self.assertEqual(start.value, 2)
        self.ll.remove_cycle()
        self.assertFalse(self.ll.has_cycle())
        self.assertEqual(self.ll.to_list(), [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
