class Solution:
    # Want to somehow use dynamic programming
    # One thing to consider is that if i<j, then:
    # if s[i] == s[j] then LPS(i,j) = 1+LPS(i+1, j-1)
    # else LPS(i,j) = max(LPS(i,j-1), LPS(i+1, j))
    def longestPalindrome(self, s: str) -> str:
        dp = [[1 if i == j else 0 for i in range(len(s))] for j in range(len(s))]
        l = 0
        r = 0
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                l = i
                r = i+1
        
        for length in range(2, len(s)):
            for start in range(len(s)-length): 
                end = start + length
                if s[start] == s[end] and dp[start+1][end-1]:
                    dp[start][end] = 1
                    if end - start > r - l:
                        l = start
                        r = end
        return s[l:r+1]