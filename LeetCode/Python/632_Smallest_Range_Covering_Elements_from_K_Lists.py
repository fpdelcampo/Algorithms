class Solution:
    # Idea is to take the smallest numbers in each array.  Take the res as (max - min).  Then, from the take a new number from the array which produced the smallest number.  Now take res = min(res, (max - min)). Repeat until done.  We will likely "run out of" elements in one array.  In that case, once that number pulled from the array that is minimal, we are done.
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        for arr in nums:
           arr.sort()        
        most = -1
        low = []
        for i in range(len(nums)):
            low.append((nums[i][0], i))
            most = max(most, nums[i][0])
        heapq.heapify(low)
        indices = len(nums) * [0]
        interval = float('inf')
        res = [-1, -1]
        while True:
            least, index = heapq.heappop(low)
            indices[index] += 1
            if most - least < interval:
                interval = most - least
                res = [least, most]
            if indices[index] == len(nums[index]):
                return res
            most = max(most, nums[index][indices[index]])
            heapq.heappush(low, (nums[index][indices[index]], index))
        return res