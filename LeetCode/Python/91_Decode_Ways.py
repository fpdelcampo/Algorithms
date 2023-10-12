class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)
        if l == 1 and s != '0':
            return 1
        dp = [1 for _ in range(l)]
        if s[0] == '0':
            return 0

        for i in range(1,len(s)):
            if s[i] == '0':
                if s[i-1] not in ['1', '2']:
                    return 0
                else:
                    dp[i] = dp[i-2]
            elif s[i-1] == '1' or (s[i-1] == '2' and int(s[i]) <= 6):
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        
        return dp[-1]