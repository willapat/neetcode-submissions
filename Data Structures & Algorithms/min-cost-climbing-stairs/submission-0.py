class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #1 or 2 steps

        costArr = [0] * len(cost)
        costArr[0] = cost[0]
        costArr[1] = cost[1]
        for i in range(2, len(cost)):
            costArr[i] = min(costArr[i- 1], costArr[i - 2]) + cost[i]
        
        return min(costArr[-1], costArr[-2])