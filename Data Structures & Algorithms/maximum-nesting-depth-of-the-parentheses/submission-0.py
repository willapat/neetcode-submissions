class Solution:
    def maxDepth(self, s: str) -> int:
        #return max number of completed parentheses
        maxPar = 0
        stack = []

        for i in range(0, len(s)):
            if s[i] == "(":
                stack.append("(")
                if len(stack) > maxPar:
                    maxPar = len(stack)

            if s[i] == ")" and stack[-1] == "(":
                stack.pop()
        
        return maxPar
            

