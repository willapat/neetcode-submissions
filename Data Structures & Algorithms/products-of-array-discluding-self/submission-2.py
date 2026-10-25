class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                prefix.append(prefix[-1] * nums[i - 1])
        
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix[i] *= suffix
            suffix *= nums[i]

        return prefix