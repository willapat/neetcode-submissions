class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #I think we want to sort the array, then when we are going through our window, the largest element
        #will always be the last in the sub-section

        left, right = 0, k
        res = []
        while right <= len(nums):
            sub = nums[left:right]
            sub.sort()
            res.append(sub[-1])
            right += 1
            left += 1
        return res
