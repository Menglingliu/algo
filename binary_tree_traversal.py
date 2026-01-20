# Binary tree traversal
class TreeNode_BST:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# pre order BST traversal
## Visit current node (V)
## Traverse left subtree (L)
## Traverse right subtree (R)

def pre_order_iter(root):
    ans = []
    cur = root
    stack = []
    while cur or stack:
        if cur:
            stack.append(cur)
            ans.append(cur.val)
            cur = cur.left
        else:
            cur = stack.pop()
            cur = cur.right
    return ans


result = []
def pre_order_rec(root):
    if not root:
        return
    result.append(root.val)
    pre_order_rec(root.left)
    pre_order_rec(root.right)
    return result


# def pre_order_BST_rec(root):
#     if not root:
#         return []
#     return [root.val] + pre_order_BST_rec(root.left) + pre_order_BST_rec(root.right)


# in order BST traversal
##Traverse left subtree (L)
##Visit current node (V)
##Traverse right subtree (R)

def in_order_iter(root):
    ans = []
    cur = root
    stack = []
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right
    return ans

result = []
def in_order_rec(root):
    if not root:
        return
    in_order_rec(root.left)        
    result.append(root.val)
    in_order_rec(root.right)
    return result

# def in_order_BST_rec(root):
#     if not root:
#         return []
#     return in_order_BST_rec(root.left) + [root.val] + in_order_BST_rec(root.right)



# post order BST traversal
##Traverse left subtree (L)
##Traverse right subtree (R)
##Visit current node (V)

def post_order_iter(root):
    ans = []
    cur = root
    stack = []
    while cur or stack:
        if cur:
            stack.append(cur)
            ans.append(cur.val)
            cur = cur.right
        else:
            cur = stack.pop()
            cur = cur.left
    return ans[::-1]

result = []
def post_order_rec(root):
    if not root:
        return
    post_order_rec(root.left)        
    post_order_rec(root.right)
    result.append(root.val)
    return result

# def post_order_BST_rec(root):
#     if not root:
#         return []
#     return post_order_BST_rec(root.left) + post_order_BST_rec(root.right) + [root.val]


# level order BFS traversal
import collections
def level_order_iter(root):
    q = collections.deque([root])
    ans = []
    while q:
        n = len(q)
        for i in range(n):
            cur = q.popleft()
            ans.append(cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
    return ans


# Test case
t4 = TreeNode_BST(4)
t5 = TreeNode_BST(5)
t7 = TreeNode_BST(7)
t6 = TreeNode_BST(6, None, t7)
t2 = TreeNode_BST(2, t4, t5)
t3 = TreeNode_BST(3, t6)
t1 = TreeNode_BST(1, t2, t3)

assert pre_order_iter(t1) == [1, 2, 4, 5, 3, 6, 7]
assert in_order_iter(t1) == [4, 2, 5, 1, 6, 7, 3]
assert post_order_iter(t1) == [4, 5, 2, 7, 6, 3, 1]
assert level_order_iter(t1) == [1, 2, 3, 4, 5, 6, 7]

assert pre_order_rec(t1) == [1, 2, 4, 5, 3, 6, 7]
assert in_order_rec(t1) == [4, 2, 5, 1, 6, 7, 3] 
assert post_order_rec(t1) == [4, 5, 2, 7, 6, 3, 1]

