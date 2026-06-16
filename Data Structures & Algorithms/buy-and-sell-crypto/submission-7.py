class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left, right = 0, 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            
            maxProfit = max(maxProfit, prices[right] - prices[left])
            right += 1
        return maxProfit
