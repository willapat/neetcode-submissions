class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            length = len(strs[i])
            res += str(length) + "#" + strs[i]
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        index = 0
        while index < len(s):
            length = ""
            while s[index].isdigit():
                length += s[index]
                index += 1
            res.append(s[index + 1:int(length) + index + 1])
            index += int(length) + 1
        
        return res
                