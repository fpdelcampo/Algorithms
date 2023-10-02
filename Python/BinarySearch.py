import unittest

def binary_search(nums, target):
    l = 0
    r = len(nums)-1
    while l <= r:
        m = (l+r)//2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m+1
        else:
            r = m-1
    return -1

# Tests by ChatGPT

class TestBinarySearch(unittest.TestCase):

    def test_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 5
        self.assertEqual(binary_search(arr, target), 4)

    def test_not_found(self):
        arr = [1, 2, 3, 4, 6, 7, 8, 9, 10]
        target = 5
        self.assertEqual(binary_search(arr, target), -1)

    def test_empty_list(self):
        arr = []
        target = 5
        self.assertEqual(binary_search(arr, target), -1)

    def test_single_element(self):
        arr = [7]
        target = 7
        self.assertEqual(binary_search(arr, target), 0)

    def test_large_list(self):
        arr = list(range(1, 10001))
        target = 7500
        self.assertEqual(binary_search(arr, target), 7499)

if __name__ == '__main__':
    unittest.main()

