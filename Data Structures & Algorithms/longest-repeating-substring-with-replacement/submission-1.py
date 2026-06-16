class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        dic = {}
        freq = 0
        left, right = 0, 0
        while right < len(s):
            dic[s[right]] = dic.get(s[right], 0) + 1

            for val in dic.values():
                freq = max(freq, val)

            while (right - left + 1) - freq > k:
                dic[s[left]] -= 1
                left += 1
            else:
                res = max(res, right - left + 1)
            right += 1
        return res

