class Solution:
    # If yes, we have a one followed by an even number of zeros
    def isPowerOfFour(self, n: int) -> bool:
        comp = ""
        for i in range(31):
            if i % 2 == 0:
                comp = "1"+comp
            else:
                comp = "0"+comp
        comp = "0b" + comp
        comp = int(comp, 2)
        print(n & (n-1), n & comp, n, comp)
        return n != 0 and n & (n-1) == 0 and (n & comp) == n