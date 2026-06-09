class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #we want to check if the numbers prev is in the set
        s = set(nums)
        total = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in s:
                long = 1
                val  = nums[i] + 1
                while val in s:
                    long += 1
                    val += 1
                if long > total:
                    total = long
        return total
