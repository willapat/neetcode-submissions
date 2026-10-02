class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        high = 0
        for i in range(len(nums)):
            curr = nums[i]
            if curr - 1 not in s:
                size = 1
                while curr + 1 in s:
                    size += 1
                    curr += 1
                high = max(high, size)
        
        return high