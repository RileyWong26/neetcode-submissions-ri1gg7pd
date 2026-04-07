class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        res = 0

        

        for i in range(len(position)):
            pos = position[i]
            spd = speed[i]

            time = (target - position[i]) / spd 

            position[i] = (pos, time)

        position.sort(reverse=True)
        print(position)
        for pos in position:
            _, dx = pos
            if len(stack) == 0:
                stack.append(dx)
            else:
                # Going to make a fleet with car infront
                if dx > stack[-1]:
                    stack.append(dx)


        return len(stack)