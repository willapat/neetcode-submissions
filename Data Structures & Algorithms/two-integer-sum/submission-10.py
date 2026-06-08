class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, n in enumerate(nums):
            val = target - n
            if val in s:
                return [s[val], i]
            s[n] = i
