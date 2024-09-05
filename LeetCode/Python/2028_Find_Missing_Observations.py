class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        s = sum(rolls)
        m = len(rolls)
        if (s + 6 * n) < (n + m) * mean:
            return []
        if (s + n) > (n + m) * mean:
            return []
        target = mean * (n + m) - s # This is the sum of the array that solves the question
        res = []
        for _ in range(n):
            # Add a valid number
            for i in range(1, 7):
                if target - i > 6 * (n-1):
                    continue
                else:
                    res.append(i)
                    break
            n -= 1
            target -= res[-1]  
        return res