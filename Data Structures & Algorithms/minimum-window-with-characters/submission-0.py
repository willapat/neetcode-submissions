class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        freq_s = {}
        freq_t = {}
        res = None

        for let in t:
            freq_t[let] = freq_t.get(let, 0) + 1
            freq_s[let] = 0
        
        have = 0
        need = len(freq_t)
        while right < len(s):
            if s[right] in freq_s:
                freq_s[s[right]] += 1
                if freq_s[s[right]] == freq_t[s[right]]:
                    have += 1

            if have == need:
                while have == need:
                    sub = s[left:right + 1]
                    if res == None or len(sub) < len(res):
                        res = sub
                    if s[left] in freq_s:
                        freq_s[s[left]] -= 1
                        if freq_s[s[left]] < freq_t[s[left]]:
                            have -= 1
                    left += 1
                    
            right += 1
        if res == None:
            return ""
        return res
                        