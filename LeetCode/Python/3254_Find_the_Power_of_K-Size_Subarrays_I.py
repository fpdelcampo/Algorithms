class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if nums == 1 or k == 1:
            return nums
        consecutive = 1
        for i in range(1, k):
            if nums[i] == nums[i - 1] + 1:
                consecutive += 1
            else:
                consecutive = 1
        res = []
        if consecutive == k:
            res.append(nums[k - 1])
        else:
            res.append(-1)
        for i in range(k, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                if consecutive >= k - 1:
                    res.append(nums[i])
                else:
                    consecutive += 1
                    res.append(-1)
            else:
                consecutive = 1
                res.append(-1)
        return res