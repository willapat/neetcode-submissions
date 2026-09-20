class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minNum = float('inf')
        piles.sort()

        def speed(rate):
            count = 0
            for i in range(len(piles)):
                count += math.ceil(piles[i] / rate)
            return count

        left, right =  1, piles[-1]
        while left <= right:
            mid = (left + right) // 2
            time = speed(mid)
            if time > h:
                left = mid + 1
            else:
                right = mid - 1
                minNum = min(minNum, mid)

        return minNum





