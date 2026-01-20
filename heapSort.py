def heapify(arr, n, cur_loc):
    # n: len of unsorted array; i: starting root
    nxt_loc = cur_loc
    l = 2 * cur_loc + 1
    r = 2 * cur_loc + 2

    # Note it is < and not <= !!
    if l < n and arr[nxt_loc] < arr[l]:
        nxt_loc = l    
    if r < n and arr[nxt_loc] < arr[r]:
        nxt_loc = r
    if nxt_loc != cur_loc:
        (arr[cur_loc], arr[nxt_loc]) = (arr[nxt_loc], arr[cur_loc])
        heapify(arr, n, nxt_loc)


def heapSort(arr):
    n = len(arr)
    # create a max heap; runtime O(n)
    for i in range(n//2, -1, -1):
        heapify(arr, n, i) 
    # sort: swap first and last element of max heap and then heapify the array with boundary set at the last item
    # repeat this process n times; each time the boundary is moved one item to the left
    # runtime O(nlogn)
    for i in range(n - 1, 0, -1):
        (arr[0], arr[i]) = (arr[i], arr[0])
        heapify(arr, i, 0)
    return arr



print(heapSort([4,7,2,5,9,4,0,19]))
assert heapSort([4,7,2,5,9,4,0,19]) == [0,2,4,4,5,7,9,19]
assert heapSort([3,1,4,6,8,9,2,2]) == [1,2,2,3,4,6,8,9]
