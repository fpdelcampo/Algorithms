class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        next = []
        for num in nums:
            next.append(int(str(num)[::-1]))
        nums.extend(next)
        return len(set(nums))