class Solution:
    def isValid(self, s: str) -> bool:
        #so essentially we want to add all open ones, and then when we reach a close\
        #pop and compare them
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                recent = stack.pop()
                if recent == '(' and s[i] != ')':
                    return False
                elif recent == '{' and s[i] != '}':
                    return False
                elif recent == '[' and s[i] != ']':
                    return False
        if len(stack) > 0:
            return False
        return True