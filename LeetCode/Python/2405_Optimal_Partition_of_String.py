class Solution:
    # Scan the string.  If we've seen a character we need to create a new substring
    def partitionString(self, s: str) -> int:
        answers = []
        seen = set()
        count = 1
        for i in s:
            if i not in seen:
                seen.add(i)
            else:
                seen = set()
                seen.add(i)
                count+=1
        return count