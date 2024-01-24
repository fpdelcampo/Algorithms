class Solution:
    def smallestSubsequence(self, s: str) -> str:
        seen = set()
        stack = []
        last = {}
        for idx, char in enumerate(s):
            last[char] = idx
        for idx, char in enumerate(s):
            if char not in seen:
                while stack and char < stack[-1] and last[stack[-1]] > idx:
                    seen.remove(stack.pop())
                seen.add(char)
                stack.append(char)
        return "".join(stack)

