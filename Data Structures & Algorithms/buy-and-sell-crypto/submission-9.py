class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = -1
        left, right = 0, 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit < 0:
                left = right
                right += 1
            else:
                maxP = max(maxP, profit)
                right += 1
        return maxP