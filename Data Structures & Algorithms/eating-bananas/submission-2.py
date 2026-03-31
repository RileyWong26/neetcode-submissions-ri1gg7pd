class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # sort ascending O(nlogn)
        piles.sort()
        
        
        # Max amount of time 
        upper_bound = piles[-1]       
        
        res = upper_bound

        l = 1
        r = upper_bound

        while(l != r):
            k = (r - l) // 2 + l

            # find amount of hours it would take to eat at this speed
            hours = 0
            for n in piles:
                hours += math.ceil(n / k)
            
            # Update res with a lower speed
            if hours <= h:
                res = min(res, k)

            # Search smaller values
            if hours <= h: 
                r =k
            elif hours > h:
                l = k + 1
            

        return res
