class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for word in strs:
            out += str(len(word)) + "#" + word
        return out
    def decode(self, s: str) -> List[str]:
        length = ""
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                length += s[j]
                j += 1
            num = int(length)
            res.append(s[j + 1 : j + 1 + num])
            length = ""
            i = j + 1 + num
        return res 
        # 5 # w a t e r 4 #
        # 0 1 2 3 4 5 6 7 8
            