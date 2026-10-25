class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        high = 0
        seen = set()
        left, right = 0, 0
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            high = max(high, right - left + 1)
            right += 1
        
        return high