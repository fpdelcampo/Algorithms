# Basically, we want to consider every triplet once
# We can use the same index repeatedly.
# XOR properties: x XOR x = 0; x XOR 0 = x
# To yield a lot of unique values, we can just have the first two indices be the same (therefore cancelling to 0). As an example with [3, 1, 2], we can just XOR each number with itself to get 0, taking i = j, and then XOR'ing that with the remaining element we desire.
# Clearly, we can generate 0 to n.
# Need to consider how high we can go.
# Suppose we have n = 101. We can go up to 111, and we also have 0, so the total is 2 ^ ceil(log2(n))
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        n = len(nums)
        return 2 ** ceil(log2(n + 1))