from list_node import *
def next_to_last(head):
    if head is None or head.next is None:
        return None
    else:
        curr = head
        # key is to get second to last so curr.next.next
        while curr.next.next is not None:
            curr = curr.next
        # wants the value of the second to last node
        return curr.val

def duplicate(head):
    curr = head
    while curr is not None:
        new_node = ListNode(curr.val)
        # set the next of new node to curr.next
        new_node.next = curr.next
        # curr.next is reassigned to new_node
        curr.next = new_node
        # curr is noe new_node.next
        curr = new_node.next
    return head
def file_to_dict(file_name):
    line_num = 0
    dicts = {}
    infile = open(file_name, "r")
    for line in infile:
        line = line.strip().split()
        if line_num % 2 == 0:
            dicts[line[0]] = line[1]
        line_num += 1
    return dicts
def palindrome_array(arr):
    if len(arr) == 0:
       return True
    else:
        rev_arr = arr[::-1]
        for i in range(len(arr)):
            temp = rev_arr.pop()
            rev_arr.insert(0, temp)
        for i in range(len(arr)):
            if arr[i] != rev_arr[i]:
                return False
    return True

def find_median_of_five():
    lst = []
    for i in range(5):
        num = int(input())
        lst.append(num)
    lst.sort()
    return lst[2]
def find_max(head):
    if head is None:
        return None
    if head.next is None:
        return head.val
    highest = None
    curr = head
    while curr is not None:
        if highest is None or curr.val > highest:
            highest = curr.val
        curr = curr.next
    return highest
def main():
    nodes   = [ ListNode(2),
                ListNode(3),
                ListNode(5),
                ListNode(7),
                ListNode(11),
                ListNode(13),
                ListNode(17),
                ListNode(19),
                ListNode(23)  ]
    in_list = nodes[0]
    nodes[0].next = nodes[1]
    nodes[1].next = nodes[2]
    nodes[2].next = nodes[3]
    nodes[3].next = nodes[4]
    nodes[4].next = nodes[5]
    nodes[5].next = nodes[6]
    nodes[6].next = nodes[7]
    nodes[7].next = nodes[8]
    # print(in_list)
    # print(next_to_last(in_list))
    #print(duplicate(in_list))
    #print(file_to_dict("example_file.txt"))
    #print(find_median_of_five())
    #print(find_max(in_list))
main()

