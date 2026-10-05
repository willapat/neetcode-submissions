class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = [0] * 52
        for char in t:
            if char.isupper():
                index = ord(char) - ord('A') + 26
            else:
                index = ord(char) - ord('a')

            freq[index] += 1
        window = [0] * 52

        sett = set(t)
        res = (float('inf'), "")
        matched = 0

        left, right = 0,0
        while right < len(s):
            char = s[right]
            if char.isupper():
                index = ord(char) - ord('A') + 26
            else:
                index = ord(char) - ord('a')
            window[index] += 1
            if window[index] == freq[index]:
                matched += 1
            while matched == len(sett):
                if right - left + 1 < res[0]:
                    res = (right - left + 1, s[left:right + 1])
                removed = s[left]
                if removed.isupper():
                    i = ord(removed) - ord('A') + 26
                else:
                    i = ord(removed) - ord('a')
                window[i] -= 1
                if window[i] < freq[i]:
                    matched -= 1
                left += 1
            right += 1
        
        return res[1]
            