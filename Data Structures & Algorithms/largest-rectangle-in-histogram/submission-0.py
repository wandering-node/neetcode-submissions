class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for idx, height in enumerate(heights):
            if not stack or stack[-1][1] <= height:
                stack.append((idx, height))
            else:
                while stack and stack[-1][1] > height:
                    last_idx, last_h = stack.pop()
                    maxArea = max(maxArea, (idx - last_idx) * last_h)
                stack.append((last_idx, height))
        while stack:
            idx, height = stack.pop()
            maxArea = max(maxArea, (len(heights) - idx) * height)
        return maxArea
