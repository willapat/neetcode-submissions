class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #with input n, return all possible combinations of parentheses
        #you can make that sum to n
        #at each spot, you either open or close parentheses
        self.res = []

        def backtrack(path, op, cl):
            if (op + cl) == n * 2 and op == cl:
                self.res.append(path)
            
            if op < n:
                path += "("
                backtrack(path, op + 1, cl)
                path = path[:-1]         
            if cl < op:
                path += ")"
                backtrack(path, op, cl + 1)
                path = path[:-1]         
                

        backtrack("", 0, 0)
        return self.res