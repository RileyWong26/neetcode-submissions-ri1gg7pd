class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = [n for n in nums]
        heapq.heapify(self.nums)

        while len(self.nums) > k:
            heapq.heappop(self.nums)

        self.k = k


    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        if len(self.nums) == 0:
            return 0
        return self.nums[0]
        
