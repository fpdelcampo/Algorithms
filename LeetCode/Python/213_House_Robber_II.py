class Solution:
    def rob(self, nums: List[int]) -> int:
        # We have two DP arrays
        # One represents the max gain from robbing houses include 0th house
        # Two represents the max gain from robbing houses excluding the 0th house
        # Then we can derive the recurrence relations and implement
        if len(nums) == 1:
            return nums[0]
        if len(nums) in [2,3]:
            return max(nums)
        
        dp1 = [0 for _ in range(len(nums))]
        dp2 = [0 for _ in range(len(nums))]
        
        dp1[0] = nums[0]
        dp1[1] = nums[0]
        dp1[2] = nums[0]
        dp1[3] = nums[0]+nums[2]

        dp2[0] = 0
        dp2[1] = nums[1]
        dp2[2] = max(nums[1], nums[2])
        dp2[3] = max(nums[2], nums[1]+nums[3])

        for i in range(4, len(nums)):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i-1])
            dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i])

        return max(dp1[-1], dp2[-1])