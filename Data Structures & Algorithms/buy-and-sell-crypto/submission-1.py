class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, l = 0, 0

        for r in range(len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else: 
                l = r
        return max_profit
