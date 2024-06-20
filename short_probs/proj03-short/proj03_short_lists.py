from list_node import *

def list_to_array(head):
    array = []
    if head is None:
        return []
    else:
        curr = head
        while curr is not None:
            array.append(curr.val)
            curr = curr.next
        return array

def array_to_list(data):
    if len(data) == 0:
        return ListNode(None)
    else:
        head = ListNode(data[0])
        curr = head
        for i in range(len(data)-1):
            node = ListNode(data[i+1])
            curr.next = node
            curr = curr.next
        return head       

        
def list_length(head):
    curr = head
    length = 0
    while curr is not None:
        length += 1
        curr = curr.next
    return length


def split_list(old_head):
    curr = old_head
    length = 0
    half = 0
    while curr is not None:
        length += 1
        curr = curr.next
    if length % 2 != 0:
        half = length // 2 
    else:
        half = (length / 2) - 1
    curr = old_head
    middle = 0
    while middle < half and curr is not None:
        middle += 1
        curr = curr.next
    new_head = curr.next
    curr.next = None
    return (old_head,new_head)


    

