class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        dic = defaultdict(int)
        left, right = 0, 0

        while right < len(s):
            val = s[right]
            dic[val] += 1
            high = 0
            for key, value in dic.items():
                high = max(high, value)
            while high + k < (right - left + 1):
                removed = s[left]
                dic[removed] -= 1
                left += 1
                for key, value in dic.items():
                    high = max(high, value)

            longest = max(longest, right - left + 1)
            right += 1

        return longest
