class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = 1
            else:
                prefix[i] = (prefix[i - 1] * nums[i - 1])

        suffix = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suffix[i] = 1
            else:
                suffix[i] = (suffix[i + 1] * nums[i + 1])
        
        res = [0] * len(nums)
        for i in range(len(suffix)):
            res[i] = prefix[i] * suffix[i]

        return res