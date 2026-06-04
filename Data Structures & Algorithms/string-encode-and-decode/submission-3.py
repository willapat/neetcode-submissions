class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for n in strs:
            encoded_string += str(len(n)) + "#" + n
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        build = ""
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded_strs.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
            
        return decoded_strs

sol = Solution()

encoded_string = sol.encode(["hello", "world"])
decoded_strs = sol.decode(encoded_string)