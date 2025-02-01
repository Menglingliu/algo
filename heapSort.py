def heapify(arr, n, i):
    # n: len of unsorted array; i: starting root
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # Note it is < and not <= !!
    if l < n and arr[largest] < arr[l]:
        largest = l    
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)
    # heapify runtime O(n), create a max heap
    for i in range(n//2, -1, -1):
        heapify(arr, n, i) 
    # Move first element of max heap to last item and then heapify the array but the last item
    # select max element and do it n times
    # runtime O(nlogn)
    for i in range(n - 1, 0, -1):
        (arr[0], arr[i]) = (arr[i], arr[0])
        heapify(arr, i, 0)
    return arr



print(heapSort([4,7,2,5,9,4,0,19]))
assert heapSort([4,7,2,5,9,4,0,19]) == [0,2,4,4,5,7,9,19]
assert heapSort([3,1,4,6,8,9,2,2]) == [1,2,2,3,4,6,8,9]
