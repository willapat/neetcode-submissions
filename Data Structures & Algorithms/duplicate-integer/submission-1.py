class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_dict = {}
        for num in nums:
            dup_dict[num] = dup_dict.get(num, 0) + 1

        for val in dup_dict.values():
            if val >= 2:
                return True

        return False