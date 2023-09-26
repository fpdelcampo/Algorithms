class Solution:
    # So we can note a few things
    # The left most letter in the substring the "smallest" letter s.t. all other letters appear after it.
    # If we find a letter which is greater than the letter after it but that also appears later on, we should use the latter appearance
    
    # Need more practice with monotonic stack
    def removeDuplicateLetters(self, s: str) -> str:
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

