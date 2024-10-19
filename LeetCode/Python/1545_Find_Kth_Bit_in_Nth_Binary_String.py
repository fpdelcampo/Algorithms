class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        for _ in range(n - 1):
            inv = "".join(["0" if char == "1" else "1" for char in s])[::-1]
            s += "1"
            s += inv
        return s[k - 1]
