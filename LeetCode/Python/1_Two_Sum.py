class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reference = {}
        answer = 0
        for idx, num in enumerate(nums):
            reference[num] = idx
        for idx, num in enumerate(nums):
            if target - num in reference and reference[target - num] != idx:
                return [idx, reference[target - num]]
        return -1