class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+n] == needle:
                return i
        return -1