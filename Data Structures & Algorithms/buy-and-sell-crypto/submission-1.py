class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_idx = 0
        # sell_idx = 0
        profit = 0
        for i in range(len(prices)):
            if prices[i] < prices[buy_idx]:
                buy_idx = i
            # sell_idx = i
            profit = max(profit, prices[i] - prices[buy_idx])
            # print(buy_idx, sell_idx, profit)
        return profit
            