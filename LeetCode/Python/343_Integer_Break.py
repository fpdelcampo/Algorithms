class Solution:
    # So basically, we want to maximize the product of ai ... ak, where they sum to n
    # f(2, 3, 4, 5) -> (1, 2, 4, 6)
    # Using AM-GM you can get a nice solution by noting that you only want to use 2 or 3
    def integerBreak(self, n: int) -> int:
        # Attempt 1:
        # Time: O(n^2)
        # Space: O(n)
        # if n in [2, 3]:
        #     return n-1
        # dp = [1 for _ in range(n+1)]
        # for i in range(1, n+1):
        #     for j in range(1, i):
        #         dp[i] = max(i, dp[i], j*dp[i-j])
        # return dp[-1]
        #
        # Attempt 2:
        # Time: O(n)
        # Space: O(n)
        #
        # dp = [0 for _ in range(n+1)]
        # if n in [2, 3]:
        #     return n-1
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, n+1):
        #     dp[i] = max(2*max(dp[i-2], i-2), 3*max(dp[i-3], i-3))
        #
        # Attempt 3:
        # Time: O(n)
        # Space: O(1)
        # if n in [2, 3]:
        #     return n-1
        # one = 2
        # two = 1
        # three = 0
        # res = 0
        # for i in range(3, n+1):
        #     res = max(2*max(two, i-2), 3*max(three, i-3))
        #     three = two
        #     two = one
        #     one = res
        # return res
        if n in [2, 3]:
            return n - 1
        if n % 3 == 0:
            return 3 ** (n//3)
        if n % 3 == 1:
            return 4 * 3 ** ((n-4)//3)            
        if n % 3 == 2:
            return 2 * 3 ** ((n-2)//3)