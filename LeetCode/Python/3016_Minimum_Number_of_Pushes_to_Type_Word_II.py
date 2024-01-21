class Solution:
    def minimumPushes(self, word: str) -> int:
        c = dict(sorted(dict(Counter(word)).items(), key = lambda x: -x[1]))
        res = 0
        used = 0
        for key in c:
            if used < 8:
                res += c[key]
                
            elif used < 16:
                res += 2*c[key]
            elif used < 24:
                res += 3*c[key]
            else:
                res += 4*c[key]
            used += 1
        return res