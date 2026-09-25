class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1
        #if right side is not equal, and its even, then its fine
        #if left side is equal, and even not fine
        mid = -1
        while left < right:
            mid = (right + left) // 2
            if mid % 2 != 0:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                # The pair is correctly aligned, so the single element
                # must be to the right.
                left = mid + 2
            else:
                # Pairing is broken, so the single element is at mid
                # or somewhere to the left.
                right = mid

        return nums[left]