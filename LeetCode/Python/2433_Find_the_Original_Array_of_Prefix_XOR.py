class Solution:
    # Key observation is that if X ^ Y = Z, then to get from X, Z to Y, we note that if Z[i] = 1, Y[i] = ~X[i], otherwise Y[i] = X[i]. So 1, x -> ~x and 0, x -> x
    # 1 0 1
    # 1 1 0
    # 0 0 0
    # 0 1 1
    # arr[i] = pref[i-1] ^ pref[i]
    def findArray(self, pref: List[int]) -> List[int]:
        res = [pref[0]]
        for i in range(1, len(pref)):
            res.append(pref[i] ^ pref[i-1])
        return res