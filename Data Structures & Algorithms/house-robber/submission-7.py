class Solution:
    def rob(self, nums: List[int]) -> int:
        #start with first or second
        money = [0] * len(nums)
        #add to index  - 2
        if len(nums) == 1:
            return nums[0]

        money[0] = nums[0]
        money[1] = nums[1]
        for i in range(2, len(nums)):
            value = nums[i]
            if i + 1 < len(nums) and nums[i + 1] > value:
                money[i + 1] = max(money[i + 1], money[i - 2] + nums[i + 1])
            money[i] = max(money[i], money[i - 2] + value)
        
        print(money)
        high = -1
        for val in money:
            high = max(high, val)
        return high