class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s))]
        for i in range(1,len(s)+1):
            if s[:i] in wordDict:
                dp[i-1] = True
            else:
                for word in wordDict:                
                    if len(word) <= i and s[i-len(word):i] == word and dp[i-len(word)-1]: 
                        dp[i-1] = True
        return dp[-1]