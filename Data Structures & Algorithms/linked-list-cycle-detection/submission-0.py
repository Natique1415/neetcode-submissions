# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #if head is None or head.next is None:
            #return False
        #else:
        visited_nodes = []
        current = head 
        while current is not None:
            if current in visited_nodes:
                return True
            else:
                visited_nodes.append(current)

            current = current.next

        return False 

    