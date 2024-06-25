from list_node import *
def is_sorted(head):
    curr = head
    if curr.next == None:
        return True
    while curr.next is not None:
        if curr.val <= curr.next.val:
            curr = curr.next
        else:
            return False
    return True
    

def list_sum(head):
    if head is None:
        return 0
    sum = 0
    curr = head
    while curr is not None:
        sum += curr.val
        curr = curr.next
    return sum

def partition_list(head):
    curr = head
    if head is None:
        return None
    index = 0 
    while head is not None:
        if index % 2 == 0:
            llist1 = curr
        else:
            llist2 = curr.next
        index += 1
        head = curr.next
        curr = None
    return llist1, llist2


def accordion_3(head, start_pos):
    # Finish
    count = 0
    if head is None:
        return None
    while head is not None and count != start_pos:
        count += 1
        head = head.next
    prev = head
    while prev.next.next.next is not None:
        curr = prev.next
        nxt = prev.next.next
        prev = prev.next.next.next
        curr = None
        nxt = None
    return head

    

def pair(list1, list2):
    curr1 = list1
    curr2 = list2
    if list1 is None or list2 is None:
        return None
    head = ListNode((curr1.val,curr2.val))
    tail = head
    while curr1.next is not None and curr2.next is not None:
        tail.next = ListNode((curr1.next.val,curr2.next.val))
        curr1 = curr1.next
        curr2 = curr2.next
        tail = tail.next
    return head
