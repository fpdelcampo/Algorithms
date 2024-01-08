class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s:
            return 0
        stack = 0
        ans = 0
        for char in s:
            if char == '(':
                stack += 1
            else:
                if stack > 0:
                    stack -= 1
                else:
                    ans += 1
        return ans + stack