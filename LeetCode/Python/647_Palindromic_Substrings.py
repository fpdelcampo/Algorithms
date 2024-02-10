class Solution:
    # Note that each character will belong to at least one palindrome.  We want to look for palindromes of maximal size (meaning the largest palindrome containing each char)
    # How many sub-palindromes exist in a palindrome?
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
        return res + len(s)