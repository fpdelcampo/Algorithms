class Solution:
    # Basically, taking XOR with x allows us to construct any number we want.
    # The maximum is then just "turning the one bit on" if the "the one bit is on" for any element
    def maximumXOR(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans = ans | num
        return ans