class Solution:
    # Observation, we only need to look for 26*26 such palindromes
    def countPalindromicSubsequence(self, s: str) -> int:
        first = {}
        last = {}
        for idx, char in enumerate(s):
            if char not in first:
                first[char] = idx
            last[char] = idx
        for key in first:
            if key not in last:
                del first[key]
        for key in last:
            if key not in first:
                del last[key]
        total = 0
        for key in first:
            if last[key] != first[key]:
                start = first[key]
                end = last[key]
                total += len(set(list(s[start+1:end])))
        return total
