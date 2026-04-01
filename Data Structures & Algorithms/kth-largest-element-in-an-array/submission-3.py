class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []
        heapq.heapify(hp)

        res = 0

        for num in nums:
            if len(hp) < k:
                heapq.heappush(hp, num)
            elif len(hp) == k:
                min = heapq.heappop(hp)
                heapq.heappush(hp, max(num, min))


        return heapq.heappop(hp)