def is_plus_two_recursive(head):
    if head.next is None:
        return True
    else:
        if head.next is not None and head.next.val == head.val + 2:
            is_plus_two_recursive(head.next)
            return True
        else:
            return False

def is_plus_two(head):
    if head is None:
        return True
    if head.next is None:
        return True
    curr = head
    while curr is not None:
        if curr.next is not None and curr.next.val != curr.val + 2:
            return False
        curr = curr.next
    return True
    
        

