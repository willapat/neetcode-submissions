class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        left, right = 0,0
        while right < len(prices):
            value = prices[right] - prices[left]
            if value < 0:
                left = right
            else:
                right += 1
                maxP = max(maxP, value)

        return maxP