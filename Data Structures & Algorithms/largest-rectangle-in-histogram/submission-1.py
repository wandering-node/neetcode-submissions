class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        for idx, height in enumerate(heights):
            if not stack or stack[-1][1] <= height:
                stack.append((idx, height))
                continue
            while stack and height < stack[-1][1]:
                last_idx, last_height = stack.pop()
                area = max(area, (idx - last_idx) * last_height)
            stack.append((last_idx, height))
        while stack:
            last_idx, height = stack.pop()
            area = max(area, (idx - last_idx + 1) * height)
        return area