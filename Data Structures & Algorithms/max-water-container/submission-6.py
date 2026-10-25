class Solution:
    def maxArea(self, heights: List[int]) -> int:
        high = -1
        left, right = 0, len(heights) - 1
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            water = width * height
            high = max(high, water)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return high