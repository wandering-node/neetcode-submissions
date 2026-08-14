class Solution:
    def maxArea(self, heights: List[int]) -> int:
        first = 0
        second = len(heights) - 1
        area = (second - first) * min(heights[first], heights[second])
        while first < second:
            if heights[first] <= heights[second]:
                first += 1

            elif heights[first] > heights[second]:
                second -= 1

            new_area = (second - first) * min(heights[first], heights[second])
            area = max(area, new_area)
        return area
