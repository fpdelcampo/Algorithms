class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        val_to_idx = {}
        for idx, num in enumerate(arr):
            if num not in val_to_idx:
                val_to_idx[num] = [idx]
            else:
                val_to_idx[num].append(idx)
        val_to_idx = dict(sorted(val_to_idx.items()))
        res = len(arr)*[0]
        i = 1
        for key in val_to_idx:
            for idx in val_to_idx[key]:
                res[idx] = i 
            i += 1
        return res