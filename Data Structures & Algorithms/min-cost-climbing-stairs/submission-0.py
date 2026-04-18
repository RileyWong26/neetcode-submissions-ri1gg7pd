class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        steps = [0] * (len(cost) + 1)

        if len(cost) > 1:
            steps[0] = 0
            if len(cost) > 2:
                steps[1] = 0

        for i in range (2, len(steps)):
            cost1 = steps[i - 1] + cost[i - 1]
            cost2 = steps[i - 2] + cost[i - 2]
            steps[i] = cost1 if cost1 < cost2 else cost2

        return steps[-1]