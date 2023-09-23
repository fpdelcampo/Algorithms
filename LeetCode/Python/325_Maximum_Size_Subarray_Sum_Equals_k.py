class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        pref = [0]
        d = {}
        d[nums[0]] = 0
        for i in range(len(nums)):
            pref.append(nums[i]+pref[-1])
            d[pref[-1]] = i+1

        # Now, we want to maximize j-i where pref[j] - pref[i] = k
        # This is now just two-sum
        max_diff = 0
        # pref[2] = -1, pref[1] = -3, pref[0] = -2
        # pref[2] - pref[0] = k
        # What if we have test case [1,1,0], k=1
        # Then we want to notice pref[2]-pref[0] = k so we should return 2
        # This fails for some reason
        
        for i in range(len(nums)):
            if k+pref[i] in d and d[k+pref[i]]>i:
                diff = d[k+pref[i]]-i
                max_diff = max(max_diff, diff)
        return max_diff