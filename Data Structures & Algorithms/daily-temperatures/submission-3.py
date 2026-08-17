class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        gaps = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            curr = temperatures[i]
            while stack and (curr > stack[-1][0]):
                temp, idx = stack.pop()
                gaps[idx] = i - idx
            stack.append((curr, i))
        return gaps
