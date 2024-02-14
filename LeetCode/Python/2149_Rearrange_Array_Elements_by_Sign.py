class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        for i in range(len(nums)):
            if i % 2 == 0:
                res.append(positive[i // 2])
            else:
                res.append(negative[i // 2])
        return res