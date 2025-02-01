import collections

def array_sum(array, target_sum):
    dict = collections.defaultdict(int)
    dict[0] = 1
    total = 0
    count = 0
    for i in array:
        total += i
        count += dict[total - target_sum]
        dict[total] += 1        
    return count


array = [1,4,3,5,-5,7,3,9]
target_sum = 7
array = [1,2,3]
target_sum = 0
print(array_sum(array, target_sum))


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    
    self.count = 0 # integer is immutable 
    total_sofar = 0
    dict_sum = collections.defaultdict(int)
    dict_sum[0] = 1
    
    def dfs(node, total_sofar):
        # nonlocal count
        if not node:
            return
        
        total_sofar += node.val
        self.count += dict_sum[total_sofar - targetSum]
        dict_sum[total_sofar] += 1
        
        dfs(node.left, total_sofar)
        dfs(node.right, total_sofar)
        
        dict_sum[total_sofar] -= 1
        
        return self.count

    return dfs(root, 0)
    
    