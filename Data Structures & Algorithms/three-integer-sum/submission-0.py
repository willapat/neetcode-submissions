class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        for i in range(len(nums)):
            target = -(nums[i])
            left = i + 1
            right = len(nums) - 1
            while left < right:
                val = nums[left] + nums[right]
                if val > target:
                    right -= 1
                elif val < target:
                    left += 1
                else:
                    if [nums[i], nums[left], nums[right]] not in res:
                        res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

        
        return res

            
            
