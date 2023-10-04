class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x in [0,1]:
            return x
        if n < 0:
            return 1/self.pow(x, -n)
        else:
            return self.pow(x, n)

    def pow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        sqrt = self.pow(x, n//2)
        if n % 2 == 0:
            return sqrt*sqrt
        else:
            return x*sqrt*sqrt