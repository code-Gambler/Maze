# A class for a min heap
class MinHeap:
    
    def __init__(self, arr=[]):
        """
        Initialize the heap with an optional initial array of elements.
        This constructor sets up the heap structure and ensures the heap property.
        """
        self.heap = []
        for element in arr:
            self.insert(element)

    def insert(self, element):
        """
        Insert an element into the heap.
        The new element is added to the end of the heap, then moved upward to its proper position.
        """
        self.heap.append(element)
        self.heapify_up(len(self.heap) - 1)

    def get_min(self):
        """
        Get the minimum element (root) of the heap.
        Returns None if the heap is empty.
        """
        if self.is_empty():
            return None
        return self.heap[0]

    def extract_min(self):
        """
        Extract and return the minimum element from the heap.
        The root element is removed and replaced with the last element, then moved downward to its proper position.
        Returns None if the heap is empty.
        """
        if self.is_empty():
            return None
        min_element = self.heap[0]
        last_element = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_element
            self.heapify_down(0)
        return min_element

    def is_empty(self):
        """
        Check if the heap is empty.
        Returns True if the heap is empty, False otherwise.
        """
        return len(self.heap) == 0

    def __len__(self):
        """
        Get the number of elements in the heap.
        Returns the count of elements in the heap.
        """
        return len(self.heap)

    def heapify_up(self, i):
        """
        Restore the heap property by moving an element up the tree.
        Compares the element with its parent and swaps if necessary, then continues recursively.
        """
        parent = (i - 1) // 2
        if parent >= 0 and self.heap[parent] > self.heap[i]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            self.heapify_up(parent)

    def heapify_down(self, i):
        """
        Restore the heap property by moving an element down the tree.
        Compares the element with its children and swaps with the smallest child if necessary, then continues recursively.
        """
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        smallest = i
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest)