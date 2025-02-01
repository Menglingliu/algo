# Binary search tree
class TreeNode:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def search(root, key):
    if not root: 
        return 
    cur = root
    while cur:
        if cur.val == key:
            return cur
        if key < cur.val:
            cur = cur.left
        else:
            cur = cur.right


def search_recursive(root, key):
    if not root:
        return
    if root.val == key:
        return root
    if key < root.val:
        return search_recursive(root.left, key)
    else:
        return search_recursive(root.right, key)


def insert(root, key):
    newnode = TreeNode(key)
    if not root:
        return newnode
    
    cur = root
    prev = None
    while cur:
        prev = cur
        if cur.val == key:
            raise Exception("key is already in the tree")
        if key < cur.val:
            cur = cur.left
        else:
            cur = cur.right
    
    if key < prev.val:
        prev.left = newnode
    else:
        prev.right = newnode
    return root


def insert_recur(root, key):
    if not root:
        return TreeNode(key)
    if root.val == key:
        raise Exception("key is already in the tree") #!!
    if key < root.val:
        root.left = insert_recur(root.left, key)
    else:
        root.right = insert_recur(root.right, key)
    return root   


def delete(root, key):
    def remove(node):  # a function to remove a node
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        head = node.right
        tail = head.left
        if not tail:
            head.left = node.left
            return head
        while tail.left:
            head = head.left
            tail = tail.left
        head.left = tail.right
        tail.left = node.left
        tail.right = node.right
        return tail
    
    if not root:
        return 
    if root.val == key:
        return remove(root)
    cur = root
    while cur:
        if cur.left and key == cur.left.val:
            cur.left = remove(cur.left)
        if cur.right and key == cur.right.val:
            cur.right = remove(cur.right)
        else:
            if key < cur.val:
                cur = cur.left
            else:
                cur = cur.right
    return root


t4 = TreeNode(4)
t5 = TreeNode(5)
t7 = TreeNode(7)
t6 = TreeNode(6, None, t7)
t2 = TreeNode(2, t4, t5)
t3 = TreeNode(3, t6)
t1 = TreeNode(1, t2, t3)

search(t1, 3)
search(t1, 3) == search_recursive(t1, 3)
insert(t1, 12)
delete(t1, 4)
