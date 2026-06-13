import heapq

class KthLargest:
    def __init__(self,k,nums):
        self.k = k
        self.heap = nums

        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self,val):
        heapq.heappush(self.heap,val)
        
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]
        

KthLargest = KthLargest(3,[4,5,8,2])
print(KthLargest.add(3))
print(KthLargest.add(5))
print(KthLargest.add(10))
print(KthLargest.add(9))
print(KthLargest.add(4))


        