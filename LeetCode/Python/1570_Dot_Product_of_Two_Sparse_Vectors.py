class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {i:v for i, v in enumerate(nums) if v != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        intersection = set(self.nums.keys()).intersection(vec.nums.keys())
        res = 0
        for key in intersection:
            res += self.nums[key] * vec.nums[key]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)