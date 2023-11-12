class Solution:
    # Key property is that elements that come before the largest don't matter since we are going to the right
    # Numbers after the largest do matter and we some how need to care about them    
    # Remember, we need n-k+1 "windows"
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        if k == len(nums):
            return [max(nums)]
        q = deque()
        res = []
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])
        for i in range(k, len(nums)):
            if q and q[0] <= i-k:
                q.popleft()
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            res.append(nums[q[0]])
        return res
