class Solution:
    # Observation: If a subarray contains x, then the minimum of that subarray is at least x.
    # Subarrays of subarrays are subarrays of the entire array (suggesting we can use DP)
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 7 + 10 ** 9
        stack = []
        n = len(arr)
        res = 0
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left[i] = i + 1 if not stack else i - stack[-1]
            stack.append(i)
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = n - i if not stack else stack[-1] - i
            stack.append(i)
        for i in range(n):
            res += arr[i] * left[i] * right[i]
            res %= MOD
        return res