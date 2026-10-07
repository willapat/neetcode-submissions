class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0

        left, right = 0,0
        while right < len(nums):
            if nums[right] == 0:
                right += 1
                left = right
            else:
                res = max(res, right - left + 1)
                right += 1
            

        return res