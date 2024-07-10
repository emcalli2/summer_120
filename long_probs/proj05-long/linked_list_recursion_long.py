""" 
    File: linked_list_recursion_long.py
    Author: Elizabeth McAllister
    Purpose: This program manipulates linked lists using recursion.
            This program contains three functions, array_to_list_recursive,
            accordion_recursive, and pairs_recursive, all three manipulate
            or use linked lists recursivly.
            This program only uses recursion, no loops.
    Class: Csc 120 Summer 2024
"""
from list_node import * 
def array_to_list_recursive(data):
    """
    This function converts an array to a linked list using recursion
    Parameters: data - an array
    Returns: a head refrence to the new linked list
    Pre-conditions: None
    """
    if data == []:
        return None
    else:
        # creates a new list node object each time
        head = ListNode(data[0])
        # links the head to the next element
        head.next = array_to_list_recursive(data[1:])
        return head

def accordion_recursive(head):
    """
    This function recursivly removes every other node after the head
    of a linked list
    Parameters: head - a linked list
    Returns: a modified linked list 
    Pre-conditions: None
    """
    if head is None:
        return None
    if head.next is None:
        return None
    else:
        # removes the head
        curr = head.next
        if curr.next is not None:
            # links the curr.next node to the next node
            curr.next = accordion_recursive(curr.next)
        return curr

def pair_recursive(head1,head2):
    """
    This function recusivly adds each node value from 
    head1 and head2 to a new linked list, presenting
    them as a tuple in each node
    Parameters: head1 - a linked list
                head 2 - another linked list
    Returns: curr - a new linked list
    Pre-conditions: None
    """
    if head1 is None:
        return None
    if head2 is None:
        return None
    else:
        curr = ListNode((head1.val, head2.val))
        curr.next = pair_recursive(head1.next, head2.next)
        return curr
         