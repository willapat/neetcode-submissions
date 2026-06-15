class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #speed = how many pos it increments
        #if cur pos  + speed >= the car ahead, then it is added to the fleet 
        dic = {}
        for x, y in zip(position, speed):
            dic[x] = y
        
        position.sort(reverse=True)
        stack = []
        for x in position:
            time = (target - x) / dic.get(x)
            if stack and stack[-1] >= time:
                None
            else:
                stack.append(time)
        return len(stack)
        