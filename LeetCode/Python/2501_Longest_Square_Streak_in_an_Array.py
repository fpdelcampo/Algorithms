class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # sqs = set([i*i for i in range(ceil(sqrt(max(nums))))])
        nums.sort()
        numbers = set(nums)
        seen = set()
        res = 0
        for num in nums:
            if num in seen:
                continue
            cnt = 1
            number = num ** 2
            seen.add(num)
            while number in numbers:
                seen.add(number)
                number = number ** 2
                cnt += 1
            res = max(res, cnt)
        return res if res > 1 else -1