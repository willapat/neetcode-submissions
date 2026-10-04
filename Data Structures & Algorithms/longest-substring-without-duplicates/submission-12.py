class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = defaultdict(int)
        longest = 0
        left, right = 0, 0

        while right < len(s):
            val = s[right]
            dic[val] += 1
            while dic[val] > 1:
                remove = s[left]
                dic[remove] -= 1
                left += 1
            longest = max(longest, right - left + 1)
            right += 1
        
        return longest