def is_plus_two_recursive(head):
    if head is None:
        print("hello")
        return True
    else:
        if head.next is not None and head.next.val == head.val + 2:
            print(head.next.val)
            print(head.val + 2)
            is_plus_two_recursive(head.next)
        return False
    
        

