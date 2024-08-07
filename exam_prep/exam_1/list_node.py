class ListNode:
    def __init__(self, val):
       self.val = val
       self.next = None
    def __str__(self):
       vals = []
       objs = set()
       curr = self
       while curr is not None:
          curr_str = str(curr.val)
          if curr in objs:
             vals.append("{} -> ... (to infinity and beyond)".format(curr_str))
             break
          else:
             vals.append(curr_str)
             objs.add(curr)
          curr = curr.next
       return " -> ".join(vals)