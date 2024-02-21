class Solution:
    # Find common prefix and return that
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        pref = 0
        while left < right:
            left >>= 1
            right >>= 1
            pref += 1
        return left << pref