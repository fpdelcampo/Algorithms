class Solution:
    # Goal is basically to find longest prefix of t in s
    # Sliding window would work but that could be too long O(len(s) * len(t))
    # Two pointers should work easily here
    def appendCharacters(self, s: str, t: str) -> int:
        l = 0
        for i in range(max(len(s), len(t))):
            if i >= len(s) or l >= len(t):
                return len(t) - l
            if s[i] == t[l]:
                l += 1
        return len(t) - l 