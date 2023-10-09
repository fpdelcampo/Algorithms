class Solution:
    # Observation: if n = len(nums), then 1 <= ans <= n+1
    # Thus, there are n choices for the answer
    # We can try the following: Take all i s.t. 1 <= v=nums[i] <= n+1 and perform a swap such that for all such i, nums[v-1] = v.  
    # Then we loop through the new array and for all j in range(1, n+1), if nums[j-1] != j, return j 
    
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums) - 1
        i = 0
        while i <= n:
            if 1 <= nums[i] < n+1 and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                i += 1
        for i in range(1, n+2):
            if nums[i-1] != i:
                return i
        return n+2
