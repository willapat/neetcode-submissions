class Solution:
    def is_integer(self, s):
        if s.startswith('-'):
            return s[1:].isdigit()
        return s.isdigit()

    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if self.is_integer(tokens[i]):
                stack.append(tokens[i])
            else:
                op = tokens[i]
                if len(stack) > 1:
                    b = int(stack.pop())
                    a = int(stack.pop())
                    output = 0
                    if op == '+': output = a + b
                    elif op == '-': output = a - b
                    elif op == '*': output = a * b
                    elif op == '/': output = int(a / b)
                    stack.append(output)
        
        return int(stack[-1])
