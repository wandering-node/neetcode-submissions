class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        gaps = [0] * length
        stack = []
        for i in range(length):
            curr = temperatures[i]
            while stack and (curr > stack[-1][0]):
                temp, idx = stack.pop()
                gaps[idx] = i - idx
            stack.append((curr, i))
        return gaps
