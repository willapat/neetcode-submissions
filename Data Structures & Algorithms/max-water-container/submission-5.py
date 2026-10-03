class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        left, right = 0, len(heights) - 1
        while left < right:
            calc = (right - left) * min(heights[left], heights[right])
            maxA = max(maxA, calc)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxA