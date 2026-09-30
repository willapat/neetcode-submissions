class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in range(0, len(nums)):
            if nums[i] in s:
                return True
            s.add(nums[i])
        return False