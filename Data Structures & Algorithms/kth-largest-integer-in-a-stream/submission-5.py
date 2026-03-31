class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.res = -9999
        heapq.heapify(nums)
        self.nums = nums
        
        while len(nums) >= k:
            self.res = max(heapq.heappop(self.nums), self.res)
        
        

    def add(self, val: int) -> int:
        if val > self.res: 
            heapq.heappush(self.nums, val)
            self.res = heapq.heappop(self.nums)

        return self.res
        
