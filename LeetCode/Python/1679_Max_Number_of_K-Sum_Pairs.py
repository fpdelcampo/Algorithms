class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        mod = Counter([k - num for num in nums])
        res = 0
        for key in mod:
            if key == k - key:
                continue
            elif key > 0 and key <= k:
                res += min(mod[key], mod[k - key])
        res //= 2
        if k % 2 == 0:
            res += mod[k // 2] // 2  
        return res