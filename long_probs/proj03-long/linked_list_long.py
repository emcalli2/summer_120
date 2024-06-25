""" 
    File: linked_list_long.py
    Author: Elizabeth McAllister
    Purpose: This program implements several functions to manipulate
            linked lists. The functions include is_sorted which checks
            if a linked list is sorted, list_sum which sums the values in
            an integer list, partition_list which returns two lists with 
            alternating values from the original, accordon_3 which returns a 
            new list following specific parameters and finally pairs which 
            combines two linked lists.
    Class: Csc 120 Summer 2024
"""
from list_node import *
def is_sorted(head):
    """ 
        This function checks weather a linked list is sorted 
        Arguments: head (a linked list)
        Return Value: True - if the list is sorted
                      False - if the list isnt sorted
        Pre-condition: None
    """
    curr = head
    if head is None:
        return True
    # if the list has one node, return True
    if curr.next == None:
        return True
    while curr.next is not None:
        if curr.val <= curr.next.val:
            curr = curr.next
        else:
            return False
    return True
    

def list_sum(head):
    """ 
        This function sums the values of an integer linked list 
        Arguments: head (an integer linked list)
        Return Value: tot_sum - the total sum of the list
        Pre-condition: None 
    """
    if head is None:
        return 0
    tot_sum = 0
    curr = head
    while curr is not None:
        tot_sum += curr.val
        curr = curr.next
    return tot_sum

def partition_list(head):
    """ 
        This function takes a single linked list and adds alternating
        values to two linked lists 
        Arguments: head (a linked list)
        Return Value: llist1 and llist2 - the two partitioned lists
        Pre-condition: None
    """
    curr = head
    index = 0
    if head is None:
        return None
    llist1 = curr
    curr1 = llist1
    llist2 = curr.next
    curr2 = llist2
    # if the list only has one node, return
    if curr.next is None:
        return llist1,llist2
    curr = curr.next.next
    while curr is not None:
        if index % 2 == 0:
            curr1.next = curr
            curr = curr.next 
            # breaks the link to the rest of the list
            curr1.next.next = None
            curr1 = curr1.next        
        else:
            curr2.next = curr
            curr = curr.next 
            # breaks the link to the rest of the list
            curr2.next.next = None 
            curr2 = curr2.next 
        index += 1
    curr2.next = None 
    return llist1,llist2


def accordion_3(head, start_pos):
    """ 
        This function starts at the node which corresponds to the 
        position of start_pos and then adds every third node to a new 
        linked list
        Arguments: head (a linked list)
                start_pos (an integer of where the new list should start)
        Return Value: llist - the new accordion list
        Pre-condition: None
    """
    count = 0
    if head is None:
        return None
    # find the start position based on start_pos
    while head is not None and count != start_pos:
        count += 1
        head = head.next
    if head is None:
        return None
    curr = head
    llist = curr
    curr1 = llist
    curr = curr.next
    index = 1 
    while curr is not None:
        if index % 3 != 0:
            curr = curr.next
        # adds every third node
        else:
            curr1.next = curr
            curr = curr.next 
            curr1.next.next = None
            curr1 = curr1.next  
        index += 1    
    return llist

    

def pair(list1, list2):
    """ 
        This function takes a pair of linked lists and merges them 
        into a single list using a tail refrence
        Arguments: list1 - a linked list
                   list2 - another linked list
        Return Value: the new list with the merged nodes
        Pre-condition: None 
    """
    curr1 = list1
    curr2 = list2
    if list1 is None or list2 is None:
        return None
    # creates a new ListNode object
    head = ListNode((curr1.val,curr2.val))
    tail = head
    while curr1.next is not None and curr2.next is not None:
        # add the new pair to the end of the list
        tail.next = ListNode((curr1.next.val,curr2.next.val))
        curr1 = curr1.next
        curr2 = curr2.next
        tail = tail.next
    return head
