class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        bought = -1
        for price in prices:
            if bought == -1:
                bought = price
            elif price < bought:
                bought = min(price, bought)
            else:
                profit += price - bought
                bought = price
        return profit