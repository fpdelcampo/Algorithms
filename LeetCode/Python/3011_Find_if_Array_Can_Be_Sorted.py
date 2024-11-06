class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        buckets = []
        bucket = [nums[0]]
        bits = bin(nums[0]).count('1')
        for i in range(1, len(nums)):
            if bin(nums[i]).count('1') == bits:
                bucket.append(nums[i])
            else:
                buckets.append(bucket)
                bits = bin(nums[i]).count('1')
                bucket = [nums[i]]
        buckets.append(bucket)
        res = []
        for bucket in buckets:
            bucket.sort()
            res.extend(bucket)
        for i in range(1, len(nums)):
            if res[i] < res[i - 1]:
                return False
        return True