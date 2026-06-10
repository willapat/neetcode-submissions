class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        left, right = 0, 0
        longest = 0
        while right < len(s):
            mp[s[right]] = mp.get(s[right], 0) + 1
            max_freq = 0
            for value in mp.values():
                if value > max_freq:
                    max_freq = value
            if (right - left + 1) - max_freq <= k:
                longest = max(longest, right - left + 1)
            else:
                while (right - left + 1) - max_freq > k:
                    mp[s[left]] -= 1
                    left += 1
            right += 1
        return longest
        
