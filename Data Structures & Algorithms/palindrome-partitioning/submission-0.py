class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #how many ways can you split up the string so that each piece is a plaindrome

        res = []
        path = []

        def backtrack(i):
            if i >= len(s):
                res.append(path[:])
                return
            
            for j in range(i, len(s)):
                string = s[i:j+1]
                if string == string[::-1]:
                    path.append(string)
                    backtrack(j+1)
                    path.pop()

        backtrack(0)
        return res
