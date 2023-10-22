class Solution:
    # Decide if you include first element then decide if you include second element ... then decide if you include last element
    # From the bottom, go back up
    # If you included the last element, exclude it
    # Go back up again
    # Recursive idea: Suppose nums is of length n, then we can return nums[0]+recurse(nums[1:]) UNION recurse(nums[1:])

    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            w = []
            for subset in subsets:
                temp = [x for x in subset]
                temp.append(num)
                w.append(temp)
            subsets.extend(w)
        return subsets
