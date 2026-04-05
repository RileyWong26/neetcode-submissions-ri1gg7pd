class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hp = []
        time = 0
        q = []


        hash = {}

        for task in tasks:
            if task not in hash:
                hash[task] = -1
            else:
                hash[task] -= 1
        
        for key in hash:
            heapq.heappush(hp, hash[key])

        res = 0 

        while len(hp) !=0 or len(q) !=0:
            if len(hp) > 0:
                num = heapq.heappop(hp)
                num +=1

                if num < 0:
                    q.append((num, time + n))
            
            if len(q) > 0:
                val, t = q[0]
                if t == time:
                    heapq.heappush(hp, val)
                    q.pop(0)
                

            time += 1


        return time
        