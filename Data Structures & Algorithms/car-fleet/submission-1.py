class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, speed = zip(*sorted(zip(position, speed), reverse=True))
        stack = []
        for i in range(len(position)):
            time = (target - position[i])/speed[i]                
            if stack and stack[-1] >= time:
                continue
            stack.append(time)
        return len(stack)
