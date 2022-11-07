class Solution:
    
    """
    
    Let dp[x] represent the minimum number of coins it takes to achieve amount x
    We can compute dp[x] as follows:
    for each coin, c
        if c<=amount (meaning we the value of coin won't make us exceed the goal amount)
            dp[i] = min(dp[i], 1+dp[i-coin]) 

    In other words, if using coin will give us a smaller result, then that's what we should do and the value of dp[i] should reflect that

    Finally, we can use this to build up to the answer such that the last element in our dp array represents the answer if possible
    If it's impossible, we will never have changed dp[-1] so it will equal 2^32, in which case we just return -1
    
    """
    
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[2**32 for _ in range(amount+1)]
        dp[0]=0
        if amount == 0:
            return 0
        for i in range(amount+1):
            for c in coins:
                if c<=amount:
                    dp[i] = min(dp[i], 1+dp[i-c])
        return -1 if dp[-1]==2**32 else dp[-1]