class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start, value):
            if value == 0:
                res.append(path[:])
                return

            if value < 0:
                return
            #i > start and 
            for i in range(start,len(nums)):
                    path.append(nums[i])
                    backtrack(i, value - nums[i])
                    path.pop()

        backtrack(0, target)
        return res