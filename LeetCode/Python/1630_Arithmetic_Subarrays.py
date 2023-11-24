class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            left = l[i]
            right = r[i]
            x = nums[left:right+1]
            x.sort()
            if len(x) in [1, 2]:
                res.append(True)
            else:
                check = True
                diff = x[1]-x[0]
                for j in range(2, len(x)):
                    if x[j] - x[j-1] != diff:
                        check = False
                res.append(check)
        return res