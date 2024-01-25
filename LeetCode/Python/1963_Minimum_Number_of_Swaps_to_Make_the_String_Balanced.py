class Solution:
    def minSwaps(self, s: str) -> int:
        left = 0
        unbalanced = 0
        for char in s:
            if char == '[':
                left += 1
            else:
                if left == 0:
                    unbalanced += 1
                else:
                    left -= 1
        return ceil(unbalanced / 2.0)