class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #of ways the numbers can be arranged, order matters
        # number of nums factorial
        res = []
        path = []
        bol = [False] * len(nums)

        def backtrack(start):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(0, len(nums)):
                if bol[i] == True:
                    continue
                path.append(nums[i])
                bol[i] = True
                backtrack(start + 1)
                path.pop()
                bol[i] = False

        backtrack(0)
        return res
                