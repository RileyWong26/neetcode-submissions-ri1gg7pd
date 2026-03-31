class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # stack containing car fleets
        fleets = []

        # Hash where the key is the position and the value is the time
        cars = {}
        for i in range(len(position)):
            cars[position[i]] = (target - position[i]) / speed[i]

        sortedKeys = sorted(cars.keys())
        # Iterate through each car position and speed
        for i in range(len(sortedKeys) - 1, -1, -1):
            
            time = cars[sortedKeys[i]]
            # no fleets just add
            if len(fleets) == 0:
                fleets.append(time)

            else:
                # this current car will be the bottle neck for the one behind. 
                if time > fleets[-1]:
                    fleets.append(time)
        
        return len(fleets)
