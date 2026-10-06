class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack and val < self.minStack[-1]: #exists and smaller
            self.minStack.append(val)
        elif self.minStack: #exists but greater
            self.minStack.append(self.minStack[-1])
        else: #intial input
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.minStack = self.minStack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
