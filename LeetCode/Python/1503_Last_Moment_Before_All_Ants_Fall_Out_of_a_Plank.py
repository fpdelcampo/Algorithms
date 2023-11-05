class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        check = []
        if left:
            check.append(max(left))
        if right:
            check.append(n-min(right))
        return max(check)