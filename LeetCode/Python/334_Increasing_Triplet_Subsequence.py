class Solution:
    # Idea is to keep track of two different first values, and two different second values
    # We do the following:
    # Initialize s1, s2 = nums[0] and m1, m2 = 2^32
    # We want the following to hold:
    # If we have an increasing pair, we want to store those values in s1, m1
    # If we have a number s.t. s1 < num < m1, we want to make m1 = x
    # If we have a number s.t. num < s1, then if m1 is unused, we have a new s1, otherwise we take s2 = num
    # Now what happens if we have two competing pairs (s1, m1) and (s2, m2), then we want to prioritize which ever one has lower m value
    # This means that we should never have (s1, m1) and (s2, m2) as being relevant going into the loop.  The only thing that matters is (s1, m1) and (s2, _)
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = 2**32
        second = 2**32
        for num in nums:
            if num > second:
                return True
            if num < first:
                first = num
            if first < num < second:
                second = num         
        return False