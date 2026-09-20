class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #we want to find longest window where replacements <= k
        l, r = 0, 0
        longest = float('-inf')
        freq = {}
        currFreq = 0
        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            for val in freq.values():
                currFreq = max(currFreq, val)
            if (r - l + 1) - currFreq <= k:
                longest = max(longest, r - l + 1)
            else:
                while (r - l + 1) - currFreq > k:
                    freq[s[l]] -= 1
                    l += 1
            r += 1
                
        
        return longest

            
