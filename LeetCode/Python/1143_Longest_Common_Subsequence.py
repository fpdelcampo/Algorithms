class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Let DP[i][j] store the longest common subsequence of text1[:i+1], text2[:j+2]
        # Let L[i][j] the indices at which the last element of the longest common subsequence occurs.
        # In other words
        # How could we find dp[i][j+1]?
        # Let len(text1) = m, len(text2) = n
        # Suppose the first characters equal each other, then DP[m][n] = 1+LCS(text1[1:], text2[1:]) (because the first character is obviously a member of the LCS)
        # Suppose they don't equal each other, then we just try "removing" the first character from the strings and run it again

        dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]
        if text1[0] == text2[0]:
            dp[0][0] = 1
        if len(text1) == len(text2) == 1:
            return dp[0][0]
        if text1[0] in text2[:2]:
            dp[0][1] = 1
        if text2[0] in text1[:2]:
            dp[1][0] = 1
        for i in range(len(text1)):
            for j in range(len(text2)):
                if (i,j) in [(0,0), (1,0), (0,1)]:
                    continue
                if text1[i]==text2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1+dp[i-1][j-1]
                else:
                    if i == 0:
                        dp[i][j] = dp[i][j-1]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]