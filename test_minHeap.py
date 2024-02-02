import unittest
from minHeap import MinHeap


class MinHeap_TestCase(unittest.TestCase):
    # These are the tests cases for functions of MinHeap class

    def test_init(self):
        the_heap = MinHeap()
        self.assertEqual(the_heap.get_min(), None)
        self.assertEqual(the_heap.extract_min(), None)

        the_heap = MinHeap([1, 2, 3, 4, 5])
        self.assertEqual(len(the_heap), 5)
        self.assertEqual(the_heap.get_min(), 1)
        self.assertEqual(len(the_heap), 5)
        self.assertEqual(the_heap.extract_min(), 1)
        self.assertEqual(len(the_heap), 4)
        self.assertEqual(the_heap.get_min(), 2)
        self.assertEqual(the_heap.extract_min(), 2)
        self.assertEqual(the_heap.get_min(), 3)
        self.assertEqual(the_heap.extract_min(), 3)
        self.assertEqual(the_heap.get_min(), 4)
        self.assertEqual(the_heap.extract_min(), 4)
        self.assertEqual(the_heap.get_min(), 5)
        self.assertEqual(the_heap.extract_min(), 5)
        self.assertEqual(len(the_heap), 0)
        self.assertEqual(the_heap.get_min(), None)
        self.assertEqual(the_heap.extract_min(), None)

    def test_insert(self):
        the_heap = MinHeap()
        the_heap.insert(1)
        self.assertEqual(the_heap.get_min(), 1)
        self.assertEqual(the_heap.extract_min(), 1)
        self.assertEqual(the_heap.get_min(), None)
        self.assertEqual(the_heap.extract_min(), None)

        the_heap = MinHeap([1, 2, 3, 4, 5])
        the_heap.insert(0)
        self.assertEqual(the_heap.get_min(), 0)
        self.assertEqual(the_heap.extract_min(), 0)
        self.assertEqual(the_heap.get_min(), 1)
        self.assertEqual(the_heap.extract_min(), 1)
        self.assertEqual(the_heap.get_min(), 2)
        self.assertEqual(the_heap.extract_min(), 2)
        self.assertEqual(the_heap.get_min(), 3)
        self.assertEqual(the_heap.extract_min(), 3)
        self.assertEqual(the_heap.get_min(), 4)
        self.assertEqual(the_heap.extract_min(), 4)
        self.assertEqual(the_heap.get_min(), 5)
        self.assertEqual(the_heap.extract_min(), 5)
        self.assertEqual(the_heap.get_min(), None)
        self.assertEqual(the_heap.extract_min(), None)

    def test_get_min1(self):
        the_heap = MinHeap()
        self.assertEqual(the_heap.get_min(), None)
        self.assertEqual(the_heap.extract_min(), None)

        the_heap = MinHeap([1, 2, 3, 4, 5])
        self.assertEqual(the_heap.get_min(), 1)
        self.assertEqual(the_heap.extract_min(), 1)
        self.assertEqual(the_heap.get_min(), 2)
        self.assertEqual(the_heap.extract_min(), 2)
        self.assertEqual(the_heap.get_min(), 3)
        self.assertEqual(the_heap.extract_min(), 3)
        self.assertEqual(the_heap.get_min(), 4)
        self.assertEqual(the_heap.extract_min(), 4)
        self.assertEqual(the_heap.get_min(), 5)
        self.assertEqual(the_heap.extract_min(), 5)
        self.assertEqual(the_heap.get_min(), None)
        self.assertEqual(the_heap.extract_min(), None)

    def test_get_min2(self):
        heap = MinHeap()
        self.assertIsNone(heap.get_min())

        heap.insert(5)
        self.assertEqual(heap.get_min(), 5)

        heap.insert(3)
        self.assertEqual(heap.get_min(), 3)

        heap.insert(8)
        self.assertEqual(heap.get_min(), 3)

        heap.insert(2)
        self.assertEqual(heap.get_min(), 2)

    def test_extract_min(self):
        the_heap = MinHeap()
        self.assertEqual(the_heap.extract_min(), None)
        self.assertEqual(the_heap.get_min(), None)

        the_heap = MinHeap([1, 2, 3, 4, 5])
        self.assertEqual(the_heap.extract_min(), 1)
        self.assertEqual(the_heap.get_min(), 2)
        self.assertEqual(the_heap.extract_min(), 2)
        self.assertEqual(the_heap.get_min(), 3)
        self.assertEqual(the_heap.extract_min(), 3)
        self.assertEqual(the_heap.get_min(), 4)
        self.assertEqual(the_heap.extract_min(), 4)
        self.assertEqual(the_heap.get_min(), 5)
        self.assertEqual(the_heap.extract_min(), 5)
        self.assertEqual(the_heap.get_min(), None)
        self.assertEqual(the_heap.extract_min(), None)

    def test_insert_duplicate_elements(self):
        heap = MinHeap()
        heap.insert(1)
        heap.insert(2)
        heap.insert(3)
        heap.insert(1)
        self.assertEqual(heap.extract_min(), 1)
        self.assertEqual(heap.extract_min(), 1)
        self.assertEqual(heap.extract_min(), 2)
        self.assertEqual(heap.extract_min(), 3)
        self.assertIsNone(heap.extract_min())

    def test_extract_from_empty_heap(self):
        heap = MinHeap()
        self.assertIsNone(heap.extract_min())

    def test_create_empty_heap(self):
        heap = MinHeap([])
        self.assertIsNone(heap.extract_min())

    def test_create_heap_with_single_element(self):
        heap = MinHeap([1])
        self.assertEqual(heap.extract_min(), 1)
        self.assertIsNone(heap.extract_min())

    def test_insert_one_element(self):
        heap = MinHeap()
        heap.insert(5)
        self.assertEqual(heap.get_min(), 5)

    def test_insert_multiple_elements(self):
        heap = MinHeap()
        heap.insert(5)
        heap.insert(3)
        heap.insert(7)
        self.assertEqual(heap.get_min(), 3)

    def test_extract_min(self):
        heap = MinHeap([5, 3, 7])
        min_val = heap.extract_min()
        self.assertEqual(min_val, 3)
        self.assertEqual(heap.get_min(), 5)

    def test_extract_min_empty_heap(self):
        heap = MinHeap()
        min_val = heap.extract_min()
        self.assertIsNone(min_val)

    def test_insert_duplicate_elements(self):
        heap = MinHeap([5, 3, 7])
        heap.insert(3)
        heap.insert(7)
        self.assertEqual(heap.get_min(), 3)

    def test_insert_descending_order(self):
        heap = MinHeap([5, 4, 3, 2, 1])
        self.assertEqual(heap.get_min(), 1)

    def test_insert_ascending_order(self):
        heap = MinHeap([1, 2, 3, 4, 5])
        self.assertEqual(heap.get_min(), 1)

    def test_extract_all_elements(self):
        heap = MinHeap([5, 3, 7])
        min_vals = []
        while heap.get_min() is not None:
            min_val = heap.extract_min()
            min_vals.append(min_val)
        self.assertEqual(min_vals, [3, 5, 7])

    def test_extract_random_order(self):
        heap = MinHeap([5, 3, 7])
        min_vals = []
        min_val = heap.extract_min()
        while min_val is not None:
            min_vals.append(min_val)
            min_val = heap.extract_min()
        self.assertEqual(min_vals, [3, 5, 7])

    def test_insert_negative_values(self):
        heap = MinHeap([-5, 3, -7])
        self.assertEqual(heap.get_min(), -7)

    def test_extract_negative_values(self):
        heap = MinHeap([-5, 3, -7])
        min_val = heap.extract_min()
        self.assertEqual(min_val, -7)

    def test_insert_float_values(self):
        heap = MinHeap([5.0, 3.0, 7.0])
        self.assertEqual(heap.get_min(), 3.0)

    def test_extract_float_values(self):
        heap = MinHeap([5.0, 3.0, 7.0])
        min_val = heap.extract_min()
        self.assertEqual(min_val, 3.0)

    def test_insert_large_heap(self):
        heap = MinHeap()
        for i in range(1000):
            heap.insert(i)
        self.assertEqual(heap.get_min(), 0)

    def test_extract_all_elements_large_heap(self):
        heap = MinHeap()
        for i in range(1000):
            heap.insert(i)
        min_vals = []
        while heap.get_min() is not None:
            min_val = heap.extract_min()
            min_vals.append(min_val)
        self.assertEqual(len(min_vals), 1000)
        self.assertEqual(min_vals[0], 0)
        self.assertEqual(min_vals[-1], 999)

    def test_insert_and_extract_random_order_large_heap(self):
        import random
        heap = MinHeap()
        for i in range(1000):
            heap.insert(random.randint(-1000, 1000))
            self.assertEqual(len(heap), i + 1)
        min_vals = []
        while heap.get_min() is not None:
            min_val = heap.extract_min()
            self.assertEqual(len(heap), 999 - len(min_vals))
            min_vals.append(min_val)
        self.assertEqual(len(min_vals), 1000)
        self.assertEqual(min_vals, sorted(min_vals))

    def test_is_empty_on_empty_heap(self):
        heap = MinHeap()
        self.assertTrue(heap.is_empty())

    def test_is_empty_on_non_empty_heap(self):
        heap = MinHeap([1, 2, 3])
        self.assertFalse(heap.is_empty())

    def test_is_empty_after_insert_and_extract(self):
        heap = MinHeap()
        heap.insert(1)
        heap.extract_min()
        self.assertTrue(heap.is_empty())

    def test_is_empty_on_large_heap(self):
        heap = MinHeap()
        for i in range(100000):
            heap.insert(i)
        for i in range(100000):
            heap.extract_min()
        self.assertTrue(heap.is_empty())

    def test_is_empty_on_large_heap_and_test_len(self):
        heap = MinHeap()
        for i in range(100000):
            heap.insert(i)
            self.assertEqual(len(heap), i + 1)
        for i in range(100000):
            heap.extract_min()
            self.assertEqual(len(heap), 99999 - i)
        self.assertTrue(heap.is_empty())
        self.assertEqual(len(heap), 0)

    def test_len_on_empty_heap(self):
        heap = MinHeap()
        self.assertEqual(len(heap), 0)

    def test_len_on_non_empty_heap(self):
        heap = MinHeap([1, 2, 3])
        self.assertEqual(len(heap), 3)


if __name__ == '__main__':
    unittest.main()
