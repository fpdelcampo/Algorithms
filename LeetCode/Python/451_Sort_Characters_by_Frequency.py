class Solution:
    def frequencySort(self, s: str) -> str:
        count = dict(sorted(dict(Counter(s)).items(), key = lambda x: -x[1]))
        res = ""
        for key in count:
            res += count[key]*key
        return res
