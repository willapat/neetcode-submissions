class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #smallest val of each array or largest of each array?
        total = len(nums1) + len(nums2)
        half = total // 2
        minArr = None
        if len(nums1) < len(nums2):
            minArr = nums1
            maxArr = nums2
        else:
            minArr = nums2
            maxArr = nums1
        
        l, r = 0, len(minArr) - 1
        while True:
            mid = (l + r) // 2
            r_half = half - mid - 2

            minLeft = minArr[mid] if mid >= 0 else float("-infinity")
            minRight = minArr[mid + 1] if (mid + 1) < len(minArr) else float("inf")
            maxLeft = maxArr[r_half] if r_half >= 0 else float("-infinity")
            maxRight = maxArr[r_half + 1] if (r_half + 1) < len(maxArr) else float("inf")
            if minLeft <= maxRight and maxLeft <= minRight:
                if total % 2 == 0:
                    return (max(minLeft, maxLeft) + min(minRight, maxRight)) / 2
                else:
                    return min(minRight, maxRight)
            elif minLeft > maxRight:
                r = mid - 1
            else:
                l = mid + 1