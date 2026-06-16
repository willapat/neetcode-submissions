class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        dup = set()
        left, right = 0, 0
        while right < len(s):
            while s[right] in dup:
                dup.remove(s[left])
                left += 1
            dup.add(s[right])
            right += 1
            res = max(res, len(dup))
        return res
