def triangle_pattern(n):
    if n == 0:
        return 
    else:
        print("*" * n)
        triangle_pattern(n-1)
#triangle_pattern(7)

# def foo(n):
#     if n == 0:
#         return
#     foo(n//2)
#     print(n)
# #foo(64)
# this functions prints 64, 32, 16, 8, 4, 2, 1
# my assumption was wrong because recusion works in revers
def foo(n):
    total = 0
    start = time.time()
    for i in range(n):
        total += i
    end = time.time()
    print(f"foo(): n={n} total={total} elapsed: {end-start} secs")
    return total
foo(1000)
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
# root = None

# root.left  = TreeNode(-31)
# root.right = TreeNode(52)

# root.left.left  = TreeNode(-50)
# root.left.right = TreeNode(-25)

# root.right.left  = TreeNode(12)
# root.right.right = TreeNode(66)

# root.right.left.left  = TreeNode(-17)
# root.right.left.right = TreeNode(50)



def invert(root):
    if root is None:
        return root
    rtree = invert(root.left)
    ltree = invert(root.right)
    root.left = ltree
    root.right = rtree

# 5) pre-order: 4,3,1,6,4,7,9
# 5) in-order: 1,6,3,4,4,9,7
# 5) post-order: 6,1,4,3,9,7,4

def reverse_array(data):
    if data == []:
        return []
    else:
        return reverse_array(data[1:]) + [data[0]]
# print(reverse_array([]))

def power(base, n):
    if n == 0:
        return 1
    else:
        return base * power(base,n-1)
#print(power(100,0))

# 8) the aspect of a binary search tree that
# allows a search to be O(logn) is that a bst 
# is left is smaller and right is larger so 
# if the value is less than the node, the only
# the left has to be searched

def count_elements(arr):
    if arr == []:
        return 0
    else:
        return 1 + count_elements(arr[1:])
#print(count_elements([1]))

def tree_height(root):
    if root is None:
        return -1 # height of an empty tree is -1
    else:
        lheight = 1 + tree_height(root.left)
        rheight = 1 + tree_height(root.right)
        if lheight > rheight:
            return lheight
        else:
            return rheight
print(tree_height(root))
def count_odd_values(arr):
    if arr == []:
        return 0
    else:
        if arr[0] % 2 != 0:
            return 1 + count_odd_values(arr[1:])
        return count_odd_values(arr[1:])
#print(count_odd_values([1]))

#12) to insert 15, it is less than 20 so go left, it is greater than 10
# so go right, is it greater than 12 so insert on the right child of 12.

#13 this function will return 28, 3  + 7 + 18

# 14) 50 will be the max of the tree from the left max 