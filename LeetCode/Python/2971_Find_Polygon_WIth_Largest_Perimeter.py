class Solution:
    # I think we want some sort of greedy approach, while also being careful that we actually construct a valid polygon
    # Dynamic programming could also work here, perhaps
    # Observation: if we cannot make a k-gon with some num x, and y > x, then the same can be said for y
    # Maybe this means we can just pull from the front of the sorted array
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        pref = [nums[0]]
        for i in range(1, len(nums)):
            pref.append(pref[-1] + nums[i])
        res = -1
        for i in range(2, len(nums)):
            if pref[i-1] > nums[i]:
                res = pref[i]
        return res
        