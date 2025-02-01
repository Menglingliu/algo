import heapq

list = [5, 7, 9, 1, 3] 
heapq.heapify(list) # turn list into minheap (min heap by default)
heapq.heappush(list, 4) # add one element into the heap and rearrange to minheap
heapq.heappop(list) # pop the min in the heap


def find_kth_largest(nums, k):
    n = len(nums)
    heapq.heapify(nums)
    i = 0
    ans = 0
    while i < n-k+1:
        ans = heapq.heappop(nums)
        i += 1
    return ans

nums = [3,2,1,5,6,4]
print(find_kth_largest(nums, k = 2))
