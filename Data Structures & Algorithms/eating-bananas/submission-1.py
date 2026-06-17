class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        piles.sort()
        left, right = 1, max(piles)
        minEat = float('inf')
        while left <= right:
            eating = (right + left) // 2
            time = h
            for val in piles:
                time -= math.ceil(val / eating)
            if time >= 0:
                minEat = min(minEat, eating)
                right = eating - 1
            else:
                left = eating + 1
        return minEat