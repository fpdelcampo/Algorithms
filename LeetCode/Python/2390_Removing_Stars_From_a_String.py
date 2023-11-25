class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        stars = 0
        for char in s:
            if char == '*':
                if stack:
                    stack.pop()
                else:
                    stars += 1
            else:
                if stars > 0:
                    stars -= 1
                else:
                    stack.append(char)
        return ''.join(stack)