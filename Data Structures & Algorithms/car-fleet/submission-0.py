class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted1, sorted2 =zip(*sorted(zip(position, speed), reverse=True))
        sorted_position = list(sorted1)
        sorted_speed = list(sorted2)
        stack = []
        fleet = 0
        for i in range(len(sorted_position)):
            time = (target - sorted_position[i])/sorted_speed[i]
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        return len(stack)
                
            
