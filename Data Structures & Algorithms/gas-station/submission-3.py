class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = -1
        prev = 0
        sum = 0
        for i in range(len(gas)):
            gas[i] = gas[i] - cost[i]
            sum += gas[i]

        if sum < 0:
            return -1

        print(gas)
        ptr = -1
        total = 0
        for i in range(len(gas)):
            total += gas[i]
            if total >=0 and ptr == -1:
                ptr = i
            elif total < 0:
                total = 0
                ptr = -1
        
        return ptr