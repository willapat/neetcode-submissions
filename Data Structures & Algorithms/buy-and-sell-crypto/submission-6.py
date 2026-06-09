class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = 0
        left = 0
        for right in range(1,len(prices)):
            profit = prices[right] - prices[left]
            if profit > 0:
                if profit > highest:
                    highest = profit
            else:
                left = right
        return highest
                

