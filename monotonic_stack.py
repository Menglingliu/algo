
def monotonic_increasing(nums):
    stack = []
    result = []

    for num in nums:
        while stack and stack[-1] > num:
            stack.pop()
        stack.append(num)

    while stack:
        result.append(stack.pop())
    
    return result[::-1]

nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(monotonic_increasing(nums))
