class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i,n in enumerate(nums):
            val = target - n
            if val in dic:
                return [dic[val], i]
            dic[n] = i

        