class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialize both cases with padding 0
        with_stock = [0] * (len(prices) + 2)
        without_stock = [0] * (len(prices) + 2)

        for i in range(len(prices) - 1, -1, -1):
            with_stock[i] = max(without_stock[i+2] + prices[i], with_stock[i+1])
            without_stock[i] = max(without_stock[i+1], with_stock[i+1]-prices[i])
        return without_stock[0]