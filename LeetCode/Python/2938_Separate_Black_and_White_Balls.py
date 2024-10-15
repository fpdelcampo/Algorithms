# We know that optimally, the ith zero belongs in the i-1th spot
class Solution:
    def minimumSteps(self, s: str) -> int:
        zero = 0
        swaps = 0
        for i in range(len(s)):
            if s[i] == '0':
                swaps += i - zero
                zero += 1
        return swaps