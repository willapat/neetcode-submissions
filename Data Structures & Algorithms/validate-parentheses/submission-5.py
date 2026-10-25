class Solution:
    def isValid(self, s: str) -> bool:
        mp = {')':'(', '}':'{', ']':'['}
        stack = []
        for char in s:
            if char in mp:
                if stack and mp[char] != stack[-1]:
                    return False
                elif stack:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if len(stack) == 0 else False