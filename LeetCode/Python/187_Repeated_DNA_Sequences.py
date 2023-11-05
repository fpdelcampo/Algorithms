# See https://leetcode.com/problems/longest-duplicate-substring/description/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        print(len(s))
        if len(s) <= 10:
            return []
        seen = set()
        for i in range(len(s)-(10-1)):
            if s[i:i+10] in seen:
                res.add(s[i:i+10])
            else:
                seen.add(s[i:i+10])
        return list(res)