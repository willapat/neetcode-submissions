class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if not dic.get(char): #if its an open
                stack.append(char)
            else:
                if stack:
                    removed = stack.pop()
                    if removed != dic[char]:
                        return False
                else:
                    return False

        return True if len(stack) == 0 else False
