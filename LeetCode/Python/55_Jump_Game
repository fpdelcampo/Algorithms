class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for _ in range(len(nums))]
        dp[-1] = True
        for i in range(len(nums)-2,-1,-1):
            cutoff = min(i+nums[i]+1,len(nums))
            for j in range(i, cutoff):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]