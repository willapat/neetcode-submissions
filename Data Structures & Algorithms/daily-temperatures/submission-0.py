class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #so in the array the number reprements like how many days until a warmer day
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res
