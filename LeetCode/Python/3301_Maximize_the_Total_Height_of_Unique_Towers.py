class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        last = maximumHeight[0]
        res = last
        for i in range(1, len(maximumHeight)):
            if maximumHeight[i] >= last:
                last -= 1
            else:
                last = maximumHeight[i]
            res += last                
        return -1 if last <= 0 else res