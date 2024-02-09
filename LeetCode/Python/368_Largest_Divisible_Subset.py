class Solution:
    # Dynamic programming does fit here.  First we sort the array.  If subset[0] | subset[1] ... subset[i] and subset[i] | potential where potential comes after subset[i] in the sorted array, we can safely add potential to our subset
    # We should also exclude duplicate numbers
    # For each i, we check all j up to i.  If the subset ending in nums[j] is bigger than the current subset at i minus 1, replace dp[i] with dp[j] and add nums[i]
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = list(set(nums))
        nums.sort()
        n = len(nums)
        dp = [[1, -1] for i in range(n)]
        for i in range(n):
            for j in range(i):   
                count1, prev1 = dp[j]
                count2, prev2 = dp[i]
                if count1 + 1 > count2 and nums[i] % nums[j] == 0:
                    dp[i] = [count1 + 1, j]
        idx = -1
        m = 0
        for i in range(n):
            if dp[i][0] > m:
                m = dp[i][0]
                idx = i
        res = [nums[idx]]
        while dp[idx][1] != -1:
            res.append(nums[dp[idx][1]])
            idx = dp[idx][1]
        return res
