import unittest
from doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()
        for value in [10, 20, 30]:
            self.dll.insert_at_tail(value)

    def test_insert_head_tail(self):
        self.dll.insert_at_head(5)
        self.dll.insert_at_tail(40)
        self.assertEqual(self.dll.to_list_forward(), [5, 10, 20, 30, 40])
        self.assertEqual(self.dll.to_list_backward(), [40, 30, 20, 10, 5])

    def test_insert_at_index(self):
        self.dll.insert_at_index(1, 15)
        self.assertEqual(self.dll.to_list_forward(), [10, 15, 20, 30])
        self.assertEqual(self.dll.to_list_backward(), [30, 20, 15, 10])

    def test_delete_at_index(self):
        self.dll.delete_at_index(1)  # delete 20
        self.assertEqual(self.dll.to_list_forward(), [10, 30])
        self.assertEqual(self.dll.to_list_backward(), [30, 10])

    def test_length(self):
        self.assertEqual(self.dll.get_length(), 3)
        self.dll.delete_at_index(0)
        self.assertEqual(self.dll.get_length(), 2)


if __name__ == "__main__":
    unittest.main()
