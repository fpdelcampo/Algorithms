class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        # xor contains x1 ^ x2
        # Now we want to split this into two groups depending on whether a particular bit is on.  If x1 = 00100111 and x2 = 01000000 for example, we could use the second bit to partition
        partition = xor & (-xor)
        x1 = 0
        x2 = 0
        for num in nums:
            if num & partition:
                x1 ^= num
            else:
                x2 ^= num
        return [x1, x2]