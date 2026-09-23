class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(1, len(nums)):
            res = nums[i - 1] ^ nums[i]
            nums[i] = res
        return nums[-1]