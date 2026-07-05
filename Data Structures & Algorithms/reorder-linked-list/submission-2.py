# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        all_nodes = []
        current = head

       # storing all the add. of nodes in the list 
        while (current is not None):
            all_nodes.append(current)
            current = current.next
        
        ln = 0 
        rn = len(all_nodes) - 1

        while ln < rn:
            
            # 1. ln.next = rn
            ln_next = all_nodes[ln + 1 ]
            all_nodes[ln].next = all_nodes[rn]
            ln += 1 

            # 2. rn.next = ln
            rn_prev = all_nodes[rn - 1]
            all_nodes[rn].next = all_nodes[ln]
            rn -= 1

        all_nodes[ln].next = None
                