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

