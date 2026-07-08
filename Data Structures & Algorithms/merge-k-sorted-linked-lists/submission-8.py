# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged_head = None 

        for i in range(len(lists)):
            if i == 0:
                merged_head = lists[i]
            else:
                merged_head = self.mergeTwoLists(merged_head,lists[i])
        
        return merged_head






    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1 
                l1 = l1.next
            
            # l1.val >= l2.val
            else:
                tail.next = l2 
                l2 = l2.next 
            
            tail = tail.next
        
        # now 
        if l1:
            tail.next = l1 

        if l2:
            tail.next = l2

        return dummy.next
        