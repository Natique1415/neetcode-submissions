# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        dummy = ListNode()
        tail = dummy

        for head in lists:
            while head:
                arr.append(head.val)
                head = head.next
        arr.sort()

        for num in arr:
            tail.next = ListNode(num)
            tail = tail.next
             
        return dummy.next

