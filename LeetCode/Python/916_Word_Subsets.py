class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        reqs = 26 * [0]
        for word in words2:
            count = 26 * [0]
            for char in word:
                count[ord(char) - ord('a')] += 1
            for i in range(26):
                reqs[i] = max(reqs[i], count[i])
        res = []
        for word in words1:
            count = 26 * [0]
            for char in word:
                count[ord(char) - ord('a')] += 1
            success = True
            for i in range(26):
                if reqs[i] > count[i]:
                    success = False
            if success:
                res.append(word)
        return res