class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        check = {}
        res = -1
        for num in nums:
            s = str(num)
            digits = 0
            for i in range(len(s)):
                digits += int(s[i])
            if digits in check:
                if len(check[digits]) == 1:
                    if check[digits][0] <= num:
                        check[digits].append(num)
                    else:
                        check[digits].append(num)
                        check[digits][0], check[digits][1] = check[digits][1], check[digits][0]
                else:
                    if check[digits][1] <= num:
                        check[digits][0], check[digits][1] = check[digits][1], num
                    elif check[digits][0] <= num:
                        check[digits][0] = num
            else:
                check[digits] = [num]
            if len(check[digits]) == 2:
                res = max(res, sum(check[digits]))
        return res