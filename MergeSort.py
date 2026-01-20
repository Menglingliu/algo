def merge(left, right):
    result = []
    index_left = index_right = 0
    while index_left < len(left) and index_right < len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else: 
            result.append(right[index_right])
            index_right += 1
    return result + left[index_left:] + right[index_right:]


def merge_sort(array):
    if len(array) <= 1: # base case!
        return array
    
    midpoint = len(array) //2

    return merge(merge_sort(array[:midpoint]), merge_sort(array[midpoint:]))

# Note there is 1 : in the code

print(merge_sort([4,7,2,5,9,4,0,19]))
assert merge_sort([4,7,2,5,9,4,0,19]) == [0,2,4,4,5,7,9,19]


# Time complexity: o(nlogn)
# Space complexity: o(n)