class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                old = stack.pop()
                res[old] = idx - old
            stack.append(idx)
        return res