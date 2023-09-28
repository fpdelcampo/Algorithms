class Solution:
    # Some things to note about the problem
    # Look at the example where minLength = 2, maxLength = 3, oneGroup = 1, zeroGroup = 2:
    # For n = 2 we have "00", "11"
    # To get n=3, we take the first solution and put 1s around it giving "001" and "100", and we take the solution "11" and just add a one
    # Note that to go from 2 to 3, we can't add 0s anywhere
    # We can store two DP arrays, one for ending in 0 and the other for ending in 1

    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        dp = [0 for _ in range(maxLength+1)]
        dp[0] = 1

        for i in range(1, maxLength+1):
            if i >= oneGroup:
                dp[i] += dp[i-oneGroup]
            if i >= zeroGroup:
                dp[i] += dp[i-zeroGroup]

        return sum(dp[minLength:maxLength+1]) % 1000000007