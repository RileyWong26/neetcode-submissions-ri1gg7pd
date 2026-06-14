class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        N = len(nums)

        res = [0 for i in range(N-k + 1)]
        l = 0
        for i in range(N):
            heapq.heappush(heap, [-1*nums[i], i])
            if l+k-1 == i:
                while len(heap) > 0:
                    val, pos = heapq.heappop(heap)
                    if pos >= l:
                        res[l] = val * -1
                        heapq.heappush(heap, [val, pos])
                        break
                l +=1
        
        return res
                        

            