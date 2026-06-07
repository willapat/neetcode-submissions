class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        high = 0
        for i in range(len(height)):
            prefix.append(high)
            if height[i] > high:
                high = height[i]
        
        suff = []
        h = 0
        for i in range(len(height) - 1, -1, -1):
            suff.append(h)
            if height[i] > h:
                h = height[i]

        suff.reverse()
        
        max_water = 0
        for i in range(len(height)):
            if min(prefix[i], suff[i]) - height[i] > 0:
                max_water += min(prefix[i], suff[i]) - height[i]

        print (prefix, suff)
        return max_water