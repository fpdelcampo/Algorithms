# First observation is that the maximum is found by taking the logical or of every element
# There are 2^16 subsets, so we can just check if each subset equals the max and then return the result
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maximum = reduce(lambda x, y: x | y, nums)
        res = 0
        subsets = [0]
        for num in nums:
            new_subset_maxs = []
            for subset_max in subsets:
                new = subset_max | num
                new_subset_maxs.append(new)
                if new == maximum:
                    res += 1
            subsets.extend(new_subset_maxs)
        return res
            
        