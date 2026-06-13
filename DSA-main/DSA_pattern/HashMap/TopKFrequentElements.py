import heapq

def topKFrequent(nums,k):
    hashmap = {}
    heap = []

    for i in range(len(nums)):
        hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1

    for key , value in hashmap.items():
        heapq.heappush(heap,(value,key))

        if len(heap) > k:
            heapq.heappop(heap)
        
    
    result = []

    for count, num in heap:
        result.append(num)

    return result
    
            
    
    

print(topKFrequent([1,1,1,2,2,3],2))
