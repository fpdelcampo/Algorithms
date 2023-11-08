class Solution:
    # either take the first non-"a" and make it an "a", or make the last element a 'b'
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        s = list(palindrome)
        idx = -1
        only = False
        for i in range(len(s)):
            if s[i] != 'a':
                if idx == -1:
                    idx = i
                else:
                    only = True
        if only:
            s[idx] = 'a'
        else:
            s[-1] = 'b'
        return ''.join(s)