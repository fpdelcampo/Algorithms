class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        x1 = sorted(s1)
        x2 = sorted(s2)
        one = True
        two = True
        for i in range(len(s1)):
            if x1[i] > x2[i]:
                one = False
            elif x1[i] < x2[i]:
                two = False
        return one or two