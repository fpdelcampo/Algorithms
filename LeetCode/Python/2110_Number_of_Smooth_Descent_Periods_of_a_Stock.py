class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        curr = 1
        total = 0
        for i in range(len(prices) -1):
            if prices[i] - prices[i+1] == 1:
                curr += 1
            else:
                total += curr * (curr + 1) // 2
                curr = 1
        total += curr * (curr + 1) // 2
        return total