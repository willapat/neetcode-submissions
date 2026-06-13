class Solution:
    def trap(self, height: List[int]) -> int:
        #if i remember we have two pointers, and we use it to like know the max height on each side
        # its like the min of the left and right - the height of the index
        maxR = 0
        maxL = 0
        left, right = 0, len(height) - 1
        res = 0
        i = 0
        while left < right:
            maxR = max(maxR, height[right])
            maxL = max(maxL, height[left])

            if min(maxR, maxL) - height[i] > 0:
                res += min(maxR, maxL) - height[i]

            if maxL > maxR:
                right -= 1
                i = right
            else:
                left += 1
                i = left
        return res
