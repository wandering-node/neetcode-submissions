from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def profit(idx: int, holding: bool) -> int:
            if idx >= len(prices):
                return 0
            if holding:
                # if i hold a stock, I can either sell it and do sth 2 days later
                sell = profit(idx + 2, False) + prices[idx]
                # or i can keep holding it, and decide what to do tomorrow
                hold = profit(idx + 1, True)
                return max(sell, hold)
            else:
                # if i don't hold any stock, I can either buy it today
                buy = profit(idx + 1, True) - prices[idx]
                # or i can rest for a day
                rest = profit(idx + 1, False)
                return max(buy, rest)

        return profit(0, False)
