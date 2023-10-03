class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        ans = 0
        for key in count:
            ans += count[key]*(count[key]-1)//2
        return ans