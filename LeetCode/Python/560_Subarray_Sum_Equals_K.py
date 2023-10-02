class Solution:
    # It's similar to two-sum but with prefix sums
    # We will use a prefix sum starting with 0, i.e., [0, 0+nums[0], 0+nums[0]+nums[1]...]
    # Sum of subarray from i to j (inclusive of i, j) = pref[j] - pref[i-1]
    # So then we want to check when k = pref[j] - pref[i-1]
    # Then we are checking for when k + pref[i-1] = pref[j]
    # This fails when k = 0 because it just takes every s.t. pref[x] = pref[x]
    # Then we can fix this by making sure that one of the prefs used has index less than another
    # Now having issues with the case [1, -1, 0], k = 0.  I can't detect that pref[3]-pref[0] = 0
    # Solution is to use 1 for loop
    # Basically this is the only way to ensure that the subarray is properly ordered
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        sums = {0:1}
        ans = 0
        for num in nums:
            prefix += num
            if prefix - k in sums:
                ans += sums[prefix - k]
            if prefix not in sums:
                sums[prefix] = 1
            else:
                sums[prefix] += 1
        return ans