class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        ans = ""
        for key in order:
            ans += count[key]*key
        for key in count:
            if key not in order:
                ans += count[key]*key
        return ans