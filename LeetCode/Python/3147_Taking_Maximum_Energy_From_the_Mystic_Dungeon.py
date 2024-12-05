class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        res = float('-inf')
        for i in range(k):
            best = None
            curr = None
            j = len(energy) - i - 1
            while j >= 0:
                if curr is not None:
                    curr += energy[j]
                    best = max(curr, best)
                else:
                    curr = energy[j]
                    best = energy[j]
                j -= k
            res = max(res, best)
        return res