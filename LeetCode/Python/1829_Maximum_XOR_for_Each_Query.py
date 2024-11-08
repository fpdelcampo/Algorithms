class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefix = [nums[0]] # prefix xor, but this is the reverse order that we need
        xor = 2 ** maximumBit - 1
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] ^ nums[i])
        res = []
        for i in range(len(nums) - 1, -1, -1):
            res.append(prefix[i] ^ (xor))
        return res