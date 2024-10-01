class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if k == 1:
            return True
        cnt = Counter([x % k for x in arr])
        for key in cnt:
            if key == 0 and cnt[key] % 2 != 0:
                return False
            if key != 0 and cnt[key] != cnt[k - key]:
                return False
        return True