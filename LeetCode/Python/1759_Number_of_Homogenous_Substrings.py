class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0
        streak = 1
        MOD = 7 + 10 ** 9
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                streak += 1
            else:
                res += (streak) * (streak + 1) // 2
                res %= MOD
                streak = 1
        return (res + (streak) * (streak + 1) // 2) % MOD