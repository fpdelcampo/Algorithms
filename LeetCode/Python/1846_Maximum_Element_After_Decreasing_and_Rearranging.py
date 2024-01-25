class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        x = 1
        for i in range(1, len(arr)):
            if arr[i] == x + 1:
                x = arr[i]
            elif arr[i] > x + 1:
                x += 1
        return x