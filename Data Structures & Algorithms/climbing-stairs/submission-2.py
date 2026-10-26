class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            staircase_low = 1
            staircase_high = 2
            for i in range(3, n+1):
                staircase_temp = staircase_high
                staircase_high = staircase_low + staircase_high
                staircase_low = staircase_temp
            return staircase_high