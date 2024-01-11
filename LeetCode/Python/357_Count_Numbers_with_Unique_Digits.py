class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        if n == 1:
            return 10

        last = 81
        s = 91
        for i in range(1, n-1):
            last *= (9 - i)
            s += last
        return s
