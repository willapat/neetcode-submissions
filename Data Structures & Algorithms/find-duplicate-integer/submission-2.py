class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #brute force would be make a set and add/compare
        #max value is the length - 1
        #min value is 1
        
        dup = 0
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                dup = abs(nums[i])
            nums[abs(nums[i]) - 1] *= -1 #MAKES THE INDEX NEGATIVE 
        return dup


        #[1,2,3,4,4]
        # 0 1 2 3 4
        # 1 2 3 4 X

        # 0 2 3 4 4
        # 