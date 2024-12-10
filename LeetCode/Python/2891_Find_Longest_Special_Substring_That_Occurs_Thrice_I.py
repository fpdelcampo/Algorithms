class Solution:
    def maximumLength(self, s: str) -> int:
        res = -1
        for i in range(1, len(s) - 1): # Checking substrings of length
            cnt = defaultdict(lambda: 0)
            for j in range(len(s) - i + 1) :
                cnt[s[j: j + i]] += 1
                if cnt[s[j: j + i]] >= 3 and s[j: j + i] == (i) * s[j]:
                    res = i
        return res