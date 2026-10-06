class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and temp > temperatures[stack[-1]]:
                days = i - stack[-1]
                res[stack[-1]] = days
                stack.pop()
            stack.append(i)

        return res