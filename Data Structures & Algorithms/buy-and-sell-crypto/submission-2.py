class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices))]
        # base case
        dp[0][0] = 0 # profit of no holding stock
        dp[0][1] = -prices[0] # profit of buying stock
        for i in range(1, len(prices)):
            # profit of not holding is either keep not holding or buy from previous date and sell today
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            # profit of buying is either bought on previous date or buy today
            dp[i][1] = max(dp[i-1][1], -prices[i])
        return max(dp[len(prices)-1][0], dp[len(prices)-1][1])