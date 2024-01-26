class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = [0 for _ in range(26)]
        for i in range(len(s)):
            last[ord(s[i]) - ord('a')] = i
        start = 0
        end = last[ord(s[0]) - ord('a')]
        res = []
        for i in range(len(s)):
            if end == i:
                res.append(i - start + 1)
                start = i + 1
                if i < len(s) - 1:
                    end = last[ord(s[i + 1]) - ord('a')]
            else:
                end = max(end, last[ord(s[i]) - ord('a')])
        if start == last[ord(s[-1]) - ord('a')]:
            res.append(1)
        return res