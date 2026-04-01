class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []
        heapq.heapify(hp)

        nums.sort()

        for i in range(len(nums) - 1, -1, -1):
            if len(hp) < k:
                heapq.heappush(hp, nums[i])
            
            if len(hp) == k:
                return heapq.heappop(hp)