import math
import unittest

# Cool thread on heap from stackoverflow: https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity

class MaxHeap:
    # Max Heap has two properties
    # 1. The value of each node is greater than or equal to the value of its parent
    # 2. The heap is a complete binary tree, meaning that it is full except for the last level, which is filled from left to right

    def __init__(self, data=[]) -> None:
        self.data = data

    def get_left(self, index): # We assume that the array is 0-indexed, so if you want the left child's index of the first element, you would pass in index=0.
        if 2*index+1 > len(self.data):
            raise ValueError(f"{2*index+1} is greater than {len(self.data)}")
        return 2*index+1

    def get_right(self, index):
        if 2*index+2 > len(self.data):
            raise ValueError(f"{2*index+2} is greater than {len(self.data)}")
        return 2*index+2

    def get_parent(self, index):
        return math.floor((index-1)/2)

    def peek(self):
        return self.data[0]

    def insert(self, value): # Inserts a node into the heap
        if not self.data:
            self.data = [value]
        else:
            self.data.append(value)
            self.heapify_up(len(self.data)-1)

    def delete(self, index): # Delete the root node
        self.data[index] = None
        self.heapify_down(index)

    def heapify_up(self, index): # Starts at index and performs heapify going upwards
        if self.data[self.get_parent(index)] < self.data[index] and index > 0:
            self.data[self.get_parent(index)], self.data[index] = self.data[index], self.data[self.get_parent(index)]
            self.heapify_up(self.get_parent(index))

    def heapify_down(self, index):
        if self.data[index] == None or self.data[index] < self.data[self.get_left(index)]:
            self.data[self.get_left(index)], self.data[index] = self.data[index], self.data[self.get_left(index)]
            self.heapify_down(self.get_left(index))

        if self.data[index] == None or self.data[index] < self.data[self.get_right(index)]:
            self.data[self.get_right(index)], self.data[index] = self.data[index], self.data[self.get_right(index)]
            self.heapify_down(self.get_right(index))
    
class TestMaxHeap(unittest.TestCase):
    def test_insert_and_peek(self):
        heap = MaxHeap()
        heap.insert(10)
        heap.insert(20)
        heap.insert(5)
        self.assertEqual(heap.peek(), 20)
    
    def test_heapify_up(self):
        heap = MaxHeap()
        heap.data = [10, 5, 3, 8, 20]
        heap.heapify_up(4)
        self.assertEqual(heap.data, [20, 10, 3, 8, 5])
    
    def test_heapify_down(self):
        heap = MaxHeap()
        heap.data = [20, 18, 10, 8, 14, 9, 3, 6, 4, 2]
        heap.heapify_down(0)
        self.assertEqual(heap.data, [20, 18, 10, 8, 14, 9, 3, 6, 4, 2])
    
    # ... Other test methods ...

# Tests by ChatGPT

if __name__ == '__main__':
    unittest.main()