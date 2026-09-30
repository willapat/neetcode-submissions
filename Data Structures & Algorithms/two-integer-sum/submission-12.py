class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value = 0
        dic = {}
        for i in range(0, len(nums)):
            if target - nums[i] in dic:
                return [dic[target - nums[i]], i]
            dic[nums[i]] = i