class Solution:
    def findMin(self, nums: List[int]) -> int:
        #rotation means shifted right + 1
        #rotations num of length is the same
        #if its been rotated, the left will be larger than right
        left, right = 0, len(nums) - 1
        minVal = float('inf')
        while left <= right:
            mid = (left + right) // 2
            minVal = min(minVal, nums[mid])
            if nums[right] >= nums[mid]:
                right = mid - 1
            elif nums[left] <= nums[mid]:
                left = mid + 1

        return minVal
            
