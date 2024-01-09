class Solution:
    # Let's say we have n = 4, k = 17
    # Note that there are 3! permutations beginning with 1, 2, 3, or 4.  So we naturally want to start the permutation with 3.  Then we have to choose the next element.  This is the same as asking us solve n = 3, k = 5, so naturally the second number is 4.  Then we are essentially solving n = 2, k = 1, so we choose 1.  Finally, we have only 2 left, so the result is 3412
    # In other words, we do math.ceil(17 / 3!) = 3.  From this, we would take 17 mod 3! = 5 and compute math.ceil(5 / 2!) = 1.  Finally we compute 5 mod 2 = 1, so we take the higher of the two remaining choices.
    def getPermutation(self, n: int, k: int) -> str:
        fact = [1] * n
        for i in range(1, n):
            fact[i] = i * fact[i-1]
        nums = [i for i in range(1, n+1)]
        k -= 1
        res = ""
        for i in range(n):
            idx = k // fact[n-i-1]
            res += str(nums[idx])
            k %= fact[n-i-1]
            nums.pop(idx)
        return res