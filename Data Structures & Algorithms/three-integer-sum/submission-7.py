class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                curSum = target + nums[l] + nums[r]
                if curSum > 0:
                    r -= 1
                elif curSum < 0:
                    l += 1
                else:
                    res.append([target, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while  l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                    while r > -1 and nums[r] == nums[r + 1]:
                        r -= 1
        
        return res

            
