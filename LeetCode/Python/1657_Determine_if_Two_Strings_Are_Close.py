class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        v1 = sorted(c1.values())
        v2 = sorted(c2.values())
        return v1 == v2 and set(word1) == set(word2)