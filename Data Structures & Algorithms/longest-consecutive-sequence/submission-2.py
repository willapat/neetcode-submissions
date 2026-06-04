class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #so it can be anywhere in the array, just how many are +1
        s = set()
        for n in nums:
            s.add(n)
        
        longest = 0
        for n in nums:
            cur = 0
            if n - 1 not in s:
                cur += 1
                while n + 1 in s:
                    cur += 1
                    n += 1
                if cur > longest:
                    longest = cur
        
        return longest


