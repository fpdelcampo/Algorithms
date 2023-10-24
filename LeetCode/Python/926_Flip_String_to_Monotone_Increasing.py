class Solution:
    # Store two DPs representing whether or not we flip to ones or zeros
    # If the next char is 0 and we flipped to zeros, no change
    # If the next char is 0 and we flipped to one, take min(DP1[i-1], DP2[i-1]+1)
    def minFlipsMonoIncr(self, s: str) -> int:
        ans = 0
        ones = 0
        for idx, char in enumerate(s):
            if char == '0':
                ans = min(ones, ans+1)
            else:
                ones += 1
        return ans