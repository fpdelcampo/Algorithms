# Seems like we can just do sliding window
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = 26 * [0]
        for char in s1:
            cnt[ord(char) - ord('a')] += 1
        seen = 26*[0]
        for start in range(len(s2)):
            if sum(seen) < len(s1):
                seen[ord(s2[start]) - ord('a')] += 1
            else:
                seen[ord(s2[start]) - ord('a')] += 1
                seen[ord(s2[start - len(s1)]) - ord('a')] -= 1
            if seen == cnt:
                return True
        return False