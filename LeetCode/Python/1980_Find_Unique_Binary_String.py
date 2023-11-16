class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return ''.join([str(int(not int(nums[i][i]))) for i in range(len(nums))])