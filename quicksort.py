from random import randint

def quicksort(array):
    if len(array) <= 1: # base case!
        return array
    
    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)] # randomly select a pivot

    # directly loop over items in the array instead of index of the array
    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        else:
            high.append(item)
    
    return quicksort(low) + same + quicksort(high)

print(quicksort([4,7,2,5,9,4,0,19]))
assert quicksort([4,7,2,5,9,4,0,19]) == [0,2,4,4,5,7,9,19]