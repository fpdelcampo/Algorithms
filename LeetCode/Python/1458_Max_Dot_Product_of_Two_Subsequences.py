class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = nums1[0] * nums2[0]
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                if i == 0 and j != 0:
                    dp[i][j] = max(dp[i][j - 1], nums1[i] * nums2[j])
                elif j == 0 and i != 0:
                    dp[i][j] = max(dp[i - 1][j], nums1[i] * nums2[j])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i-1][j-1] + nums1[i] * nums2[j], nums1[i] * nums2[j])
        return dp[-1][-1]