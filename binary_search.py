
# iterative version:
def binary_search_1(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high: 
        mid = low + (high - low) // 2
        if target < arr[mid]:
            high = mid - 1
        elif target > arr[mid]:
            low = mid + 1
        else:
            return mid 
    return -1

# recursive version:
def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if target < arr[mid]:
        return binary_search_recursive(arr, target, low, mid - 1)
    elif target > arr[mid]:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return mid


# return the first item matches with target
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        # find the first element in the arr satisfy with the constraint
        if target <= arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    if low < len(arr) and arr[low] == target:
        return low
    return -1

# "=" should appear together with "high", as we always return low


array = [2, 3, 5, 6, 7, 9, 12]
assert binary_search(array, 100) == -1
assert binary_search(array, 7) == 4
assert binary_search(array, 6) == 3


assert binary_search_1(array, 7) == 4
assert binary_search_1(array, 6) == 3



#bisect_left: return the position of an array where we insert one value into the array
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        return [len(potions) - bisect_left(potions, (success + a - 1) // a) for a in spells]