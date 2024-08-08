import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    
    def setUp(self):
        self.ll = LinkedList()

    def test_append(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        self.assertEqual(self.ll.head.data, 1)
        self.assertEqual(self.ll.head.next.data, 2)
        self.assertEqual(self.ll.head.next.next.data, 3)

    def test_prepend(self):
        self.ll.prepend(0)
        self.assertEqual(self.ll.head.data, 0)

    def test_position_insert(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.position_insert(1, 1.5)
        self.assertEqual(self.ll.head.next.data, 1.5)
        
    #def test_position_insert_invalid(self):
        #with self.assertRaises(ValueError):
            #self.ll.position_insert(-1, 1)

if __name__ == '__main__':
    unittest.main()
