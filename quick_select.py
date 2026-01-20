# quick select: find the kth smallest elements in an unordered array

import random

def quick_select(l, r, k):
    p = l
    idx = random.randint(l, r)
    pivot = nums[idx]
    nums[idx], nums[r] = nums[r], nums[idx]

    for i in range(l, r):
        if nums[i] <= pivot:
            nums[p], nums[i] = nums[i], nums[p]
            p += 1
    nums[p], nums[r] = nums[r], nums[p]

    if p < k:
        return quick_select(p+1, r, k)
    elif p > k:
        return quick_select(l, p-1, k)
    else:
        return nums[p]

nums = [3,2,1,5,6,4]
k = 3
print(quick_select(0, len(nums)-1, k-1))

# time complexity: o(n) on average; worst case: o(n^2)
# space complexity: o(n)


import random
from typing import List

def quickselect(nums: List[int], k: int) -> int:
    """
    Return the k-th smallest element (0-indexed) using in-place Quickselect.
    Average time: O(n), worst: O(n^2), extra space: O(1).
    """
    if not 0 <= k < len(nums):
        raise ValueError("k out of range")

    left, right = 0, len(nums) - 1

    while left <= right:
        # Random pivot to avoid worst-case patterns
        pivot_idx = random.randint(left, right)
        pivot_val = nums[pivot_idx]

        # Move pivot to end (Lomuto partition setup)
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

        # Lomuto partition: elements < pivot to the left
        store = left
        for i in range(left, right):
            if nums[i] < pivot_val:
                nums[store], nums[i] = nums[i], nums[store]
                store += 1

        # Move pivot into its final place
        nums[store], nums[right] = nums[right], nums[store]
        p = store  # pivot final index

        if p == k:
            return nums[p]
        elif k < p:
            right = p - 1
        else:
            left = p + 1
    # Should never get here if input is valid
    raise RuntimeError("Quickselect failed unexpectedly")

print(quickselect([3,2,1,5,6,4], 3))