class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            stack.append(i)
            if len(stack) >= 2 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
        return "".join(stack)