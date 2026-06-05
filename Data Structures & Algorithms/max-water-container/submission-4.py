class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # so essentially what height times width has the greatest area
        # we can get their height from the arr value, and then the dif between the
        # index is the width then just multiply, check if greater then update if so
        
        maxWater = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            width = right - left
            min_height = min(heights[left], heights[right])
            area = width * min_height
            if area > maxWater:
                maxWater = area
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxWater