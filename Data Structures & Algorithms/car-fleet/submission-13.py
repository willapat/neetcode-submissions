class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dic = {}
        for i in range(len(position)):
            num = (target - position[i]) / speed[i]
            dic[position[i]] = num
        
        dic = sorted(dic.items())
        stack = []
        for i in range(len(dic)):
            if stack:
                prevS = stack[-1][1]
                if dic[i][1] < prevS:
                    stack.append(dic[i])
                elif dic[i][1] > prevS:
                    while stack and dic[i][1] > stack[-1][1]:
                        stack.pop()
                    stack.append(dic[i])
            else:
                stack.append(dic[i])
        print(stack)
        return len(stack)
