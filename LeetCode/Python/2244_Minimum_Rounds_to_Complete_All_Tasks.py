class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c = Counter(tasks)
        res = 0
        for key in c:
            if c[key] == 1:
                return -1
            else:
                if c[key] % 3 == 0:
                    res += c[key] // 3
                elif c[key] % 3 == 1:
                    res += 2 + (c[key] - 4) // 3
                else:
                    res += 1 + (c[key] - 1) // 3
        return res
