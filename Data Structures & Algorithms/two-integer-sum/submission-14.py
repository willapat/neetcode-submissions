class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            valNeed = target - nums[i]
            if mp.get(valNeed) is not None:
                return [mp[valNeed], i]
            mp[nums[i]] = i