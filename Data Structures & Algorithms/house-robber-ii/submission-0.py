class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        def dfs(index, arr):
            if index >= len(arr):
                return 0
            
            if dp[index] > 0:
                return dp[index]


            dp[index] = max(arr[index] + dfs(index + 2, arr), dfs(index + 1, arr))
            return dp[index]
        

        first = []
        second = []
        for i in range(len(nums)):
            if i == 0:
                first.append(nums[i])
            elif i == len(nums) - 1:
                second.append(nums[i])
            else:
                first.append(nums[i])
                second.append(nums[i])
        
        f = dfs(0, first)
        dp = [0] * len(nums)
        s = dfs(0, second)
        return max(f, s)
        