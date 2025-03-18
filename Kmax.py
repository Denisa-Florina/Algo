import heapq

def kth_largest(nums, k):
    min_heap = nums[:k] #luam primele k elemente
    heapq.heapify(min_heap) 

    for num in nums[k:]:
        if num > min_heap[0]: #adaugam doar elementele mai mari decat cele din lista
            heapq.heappushpop(min_heap, num)

    return min_heap[0] #al k-lea cel mai mic element din cele mai mari

def kth_smaller(nums, k):
    nums = [-num for num in nums]
    max_heap = nums[:k]
    heapq.heapify(max_heap)

    for num in nums[k:]:
        if num < max_heap[0]:
            heapq.heappushpop(max_heap, num)

    return -max_heap[0]

print(kth_largest([1,2,3,4,5,6,7], 2))
print(kth_smaller([1,2,3,4,5,6,7], 2))
