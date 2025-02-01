def InsertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

print(InsertionSort([4,7,2,5,9,4,0,19]))
assert InsertionSort([4,7,2,5,9,4,0,19]) == [0,2,4,4,5,7,9,19]