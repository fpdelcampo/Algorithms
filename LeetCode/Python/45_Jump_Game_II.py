class Solution:
    # O(n^2) DP
    # def jump(self, nums: List[int]) -> int:
    #     size = len(nums)
    #     dp = [size for _ in range(size)]
    #     dp[-1] = 0
    #     if size == 1:
    #         return dp[-1]
    #     for i in range(size-2, -1, -1):
    #         for j in range(1, min(nums[i]+1, size-i)):
    #             dp[i] = min(dp[i], 1+dp[i+j])
    #     return dp[0]
    # There's probably a better way
    # We can use a greedy solution somehow
    # Basically, we keep track of how far we can go at a given jump
    # After we traverse up to the end of the jump, set end equal to wherever we are
    # Then increment answers and we repeat
    
    def jump(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return 0

        depth = 0
        end = 0
        answer = 0

        for i in range(len(nums)-1):
            depth = max(depth, nums[i] + i)
            if i>=end:
                end = depth
                answer += 1
        return answer
