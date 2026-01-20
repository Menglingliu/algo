def SelectionSort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        (array[i], array[min_index]) = (array[min_index], array[i])
    return array

print(SelectionSort([4,7,2,5,9,4,0,19]))
assert SelectionSort([4,7,2,5,9,4,0,19]) == [0,2,4,4,5,7,9,19]

# Time complexity: o(n^2)
# Space complexity: o(1)