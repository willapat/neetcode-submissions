class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[left] < nums[right]:
                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            elif nums[mid] >= nums[left] and (target > nums[mid] or target < nums[left]):
                if nums[mid] == target:
                    return mid
                left = mid + 1
            else:
                if nums[mid] == target:
                    return mid
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1