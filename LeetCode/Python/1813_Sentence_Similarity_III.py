class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2 or not sentence1 or not sentence2:
            return True
        s1 = sentence1.split()
        s2 = sentence2.split()
        if len(s1) == len(s2):
            return False
        small, big = None, None
        if len(s1) > len(s2):
            small = s2
            big = s1
        else:
            small = s1
            big = s2
        i = 0
        while i < len(small) and small[i] == big[i]:
            i += 1
        m, n = len(small) - 1, len(big) - 1
        while m >= 0 and small[m] == big[n]:
            m -= 1
            n -= 1
        return m < i