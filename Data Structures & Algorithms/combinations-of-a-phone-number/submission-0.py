class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digMap = {2: "abc", 3: "def", 4 :"ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        res = []
        self.path = ""

        def backtrack(index):
            if index >= len(digits):
                if len(self.path) > 0:
                    res.append(self.path)
                return 

            val = int(digits[index])
            for i in range(len(digMap[val])):
                self.path += (digMap[val][i])
                backtrack(index + 1)
                self.path = self.path[:-1]

        backtrack(0)
        return res