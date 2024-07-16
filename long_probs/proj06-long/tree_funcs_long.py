""" 
    File: tree_funcs_long.py
    Author: Elizabeth McAllister
    Purpose: This program contains nine functions that 
            preform different opperations on or involving 
            trees, such as searching, finding a max, or printing
            out a traversal of the tree. 
    Class: Csc 120 Summer 2024
"""
from tree_node import *

def bst_search_loop(root,val):
    """
    This function uses a while loop to search a 
    tree for a value (val). If it finds the value in
    the tree it returns that node.
    Parameters: root - a binary search tree
                val - a given value
    Returns: root - the node whos value matches val
            None - if val is not found in the tree
    """

    if root is None:
        return None
    else:
        while root is not None :
            if root.val == val:
                return root
            if root.val > val:
                root = root.left
            else:
                root = root.right
        return None

def tree_search(root,val):
    """
    This function searches any binary tree for a value (val).
    This function uses recursion
    Parameters: root - a binary tree
    Return: the node in which the val is found
    Pre - conditions: not necessarly a BST
    """
    if root is None:
        return
    if root.val == val:
        return root
    # searches the left side for the val
    lsearch = tree_search(root.left,val)
    if lsearch is not None:
        return lsearch
    # searches the right side for the val
    rsearch = tree_search(root.right,val)
    if rsearch is not None:
        return rsearch
    return None

def bst_insert_loop(root,val):
    """
    This function inserts a value (val) into a 
    binary search tree using a while loop.
    Parameters: root - a BST
                val - a given value to be inserted
    Returns: None
    """
    prev = None
    while root is not None:
        prev = root
        if val < root.val:
            root = root.left
        else:
            root = root.right
    if val < prev.val:
        prev.left = TreeNode(val)
    else:
        prev.right = TreeNode(val)

def pre_order_traversal_print(root):
    """
    This function prints out the pre order
    traversal of a tree.
    Parameters: root - a tree
    Returns: None
    """
    if root is None:
        return
    print(root.val)
    pre_order_traversal_print(root.left)
    pre_order_traversal_print(root.right)

def in_order_traversal_print(root):
    """
    This function prints out the in order
    traversal of a tree.
    Parameters: root - a tree
    Returns: None
    """
    if root is None:
        return
    in_order_traversal_print(root.left)
    print(root.val)
    in_order_traversal_print(root.right)

def post_order_traversal_print(root):
    """
    This function prints out the post order
    traversal of a tree.
    Parameters: root - a tree
    Returns: None
    """
    if root is None:
        return
    post_order_traversal_print(root.left)
    post_order_traversal_print(root.right)
    print(root.val)

def in_order_vals(root):
    """
    This function returns out the in order
    traversal of a tree as an array.
    Parameters: root - a tree
    Returns: the inorder traversal of the tree as 
            a list
    """
    if root is None:
        return []
    return in_order_vals(root.left) + [root.val] + in_order_vals(root.right)


def bst_max(root):
    """
    This function returns the max of a binary
    search tree. With bst we know that the 
    right node is always larger, thus this function
    only recurses on the right side.
    Parameters: root - a BST
    Returns: rmax - if the right side max is larger than 
                    maxi(the initial root value)
            maxi - if the right side max is less than
                    the initial root value
    """
    if root is None:
        return
    maxi = root.val
    # finds the max of the right side
    rmax = bst_max(root.right)
    if rmax is not None and rmax > maxi:
        return  rmax
    return maxi
    
def tree_max(root):
    """ 
    This function returns the max value in a tree.
    Parameters: root- a tree
    Returns: maxi - the max value in the tree
    """
    if root is None:
        return
    maxi = root.val
    # finds the max of the left side
    lmax = tree_max(root.left)
    # finds the max of the right side
    rmax = tree_max(root.right)
    if lmax is not None and lmax > maxi:
        maxi = lmax
    if rmax is not None and rmax > maxi:
        maxi = rmax
    return maxi