class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy, max_profit = prices[0], 0

        for price in prices:
            max_profit = max(max_profit, price - min_buy)
            min_buy = min(min_buy, price)

        return max_profit