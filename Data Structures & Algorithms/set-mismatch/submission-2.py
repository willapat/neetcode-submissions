class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        res = []
        for i in range(0, len(nums)):
            if nums[i] in s:
                res.append(nums[i])
            s.add(nums[i])
        
        for i in range(1, len(nums) + 1):
            if i not in s:
                res.append(i)
                return res