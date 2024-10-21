# Simple backtracking for each starting substring, try to add a subsequent substring. If it's not in use, continue! Otherwise, move to the next substring

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res = 0
        def backtrack(s, start, hashset):
            nonlocal res
            if start == len(s):
                res = max(res, len(hashset))
            for end in range(start, len(s)):
                if s[start:end + 1] not in hashset:
                    hashset.add(s[start:end + 1])
                    backtrack(s, end + 1, hashset)
                    hashset.remove(s[start:end + 1])
        backtrack(s, 0, set())
        return res