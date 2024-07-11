def tree_count(root):
    if root is None:
        return 0
    else:
        return 1 + tree_count(root.left) + tree_count(root.right)

def tree_count_1_child(root):
    if root is None:
        return 0
    else:
        if root.left is not None and root.right is not None:
            return tree_count_1_child(root.left) + tree_count_1_child(root.right)
        if root.right is None and root.left is None:
            return tree_count_1_child(root.left) + tree_count_1_child(root.right)
        else:
            return 1 + tree_count_1_child(root.left) + tree_count_1_child(root.right)

def tree_sum(root):
    if root is None:
        return 0
    else:
        return root.val + tree_sum(root.right) + tree_sum(root.left)

def tree_print(root):
    if root is None:
        return
    else:
        tree_print(root.left)
        print(root.val)
        tree_print(root.right)

def tree_print_leaves(root):
    if root is None:
        return
    else:
        if root.right is None and root.left is None:
            print(root.val)
        tree_print_leaves(root.left)
        tree_print_leaves(root.right)

def tree_search(root,val):
    if root is None:
        return
    if root.val == val:
        return root
    lsearch = tree_search(root.left,val)
    if lsearch is not None:
        return lsearch
    rsearch = tree_search(root.right,val)
    if rsearch is not None:
        return rsearch
    return None

def tree_max(root):
    max_val = root.val
    if root.left is not None:
        lmax = tree_max(root.left)
        if lmax > max_val:
            max_val = lmax
    if root.right is not None:
        rmax = tree_max(root.right)
        if rmax > max_val:
            max_val = rmax
    return max_val