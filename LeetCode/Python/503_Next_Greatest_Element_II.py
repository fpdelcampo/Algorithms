class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Idea is we make a stack monotonic stack
        stack = []
        n = len(nums)
        res = n * [0]
        high = max(nums)
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                res[idx] = nums[i]
            if nums[i] == high:
                res[i] = -1
            else:
                stack.append(i)
        if stack:
            for i in range(stack[0]):
                while stack and nums[stack[-1]] < nums[i]:
                    idx = stack.pop()
                    res[idx] = nums[i]
                stack.append(i)
        return res