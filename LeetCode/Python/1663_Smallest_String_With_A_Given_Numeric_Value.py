class Solution:
    # Goal is to use the least amount of "numbers" at the start
    # Think about when this is impossible?
    # If we had k = 27, n = 1, we wouldn't be able to solve the problem.  More generally, if we have k >= 26n + 1, we can't solve the problem.
    # Answer comes in the form a repeated x times, some letter, repeated 1 time, and z, repeated y times.  Here, x and y are both >= 0
    def getSmallestString(self, n: int, k: int) -> str:
        res = ""
        while k <= 26 * (n - 1):
            res += 'a'
            n -= 1
            k -= 1
        if k % 26:
            res += chr(ord('a') + k % 26 - 1)
        res += (k // 26) * 'z'
        return res