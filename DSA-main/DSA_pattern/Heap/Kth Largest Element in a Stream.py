# Question : Kth Largest Element in a Stream
# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Example 1:
# Input: 
# 


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



# Explanation :
# We use a min heap to store the k largest elements.
# The smallest element in the heap is the kth largest element.
# When we add a new element, we push it to the heap.
# If the size of the heap exceeds k, we pop the smallest element.
# Time Complexity : O(log k)
# Space Complexity : O(k)
# 


        