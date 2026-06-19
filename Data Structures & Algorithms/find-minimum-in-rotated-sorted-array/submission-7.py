class Solution:
    def findMin(self, nums: List[int]) -> int:
        #rotation means shifted right + 1
        #rotations num of length is the same
        #if its been rotated, the left will be larger than right
        left, right = 0, len(nums) - 1
        minVal = nums[0]
        while left <= right:
            if nums[left] < nums[right]:
                minVal = min(minVal, nums[left])
                break

            mid = (left + right) // 2
            minVal = min(minVal, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return minVal
            
