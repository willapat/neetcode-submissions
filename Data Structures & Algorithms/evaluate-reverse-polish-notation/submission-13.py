class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            cur = tokens[i]
            if cur.lstrip("-").isdigit():
                stack.append(int(cur))
            elif cur == '+':
                second = stack.pop()
                first = stack.pop()
                stack.append(first + second)
            elif cur == '-':
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            elif cur == '*':
                second = stack.pop()
                first = stack.pop()
                stack.append(first * second)
            else:
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first / second))
        
        return stack[-1]
