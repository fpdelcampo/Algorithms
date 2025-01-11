class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        cnt = Counter(s)
        odd = 0
        for key in cnt:
            if cnt[key] % 2 == 1:
                odd += 1
        return odd <= k and k <= len(s)