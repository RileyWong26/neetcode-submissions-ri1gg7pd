class MedianFinder:

    def __init__(self):
        self.preHeap = []
        self.postHeap = []

    def addNum(self, num: int) -> None:
        if len(self.preHeap) == 0:
            heapq.heappush(self.preHeap, num*-1)
        # Bigger than current med
        elif num*-1 <= self.preHeap[0]:
            heapq.heappush(self.postHeap, num)
            if len(self.postHeap) - len(self.preHeap) > 0:
                heapq.heappush(self.preHeap, -1*heapq.heappop(self.postHeap))
        
        # smaller than current med
        else:
            heapq.heappush(self.preHeap, (-1*num))
            if len(self.preHeap) - len(self.postHeap) > 0:
                heapq.heappush(self.postHeap, -1*heapq.heappop(self.preHeap))
        


    def findMedian(self) -> float:
        if len(self.preHeap) == len(self.postHeap):
            return (self.preHeap[0]*-1 + self.postHeap[0] ) /2 
        
        return self.preHeap[0]*-1 if len(self.preHeap) > len(self.postHeap) else self.postHeap[0]
        