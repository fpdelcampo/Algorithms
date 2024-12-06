class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        loc = {}
        for i in range(len(nums)):
            loc[nums[i]] = i
        for i in range(len(operations)):
            x, y = operations[i]
            idx = loc[x]
            nums[loc[x]] = y
            del loc[x]
            loc[y] = idx
        return nums