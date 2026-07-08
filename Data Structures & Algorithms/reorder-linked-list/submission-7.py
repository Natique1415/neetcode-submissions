# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle-most node
        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # slow will now pointing to the middle-most element
        second = slow.next
        slow.next = None

        # rev. the second half of the list
        prev = None
        current = second
        while current is not None:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp

        # now we will merge the 2 linked lists
        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second 
            second.next = tmp1

            first = tmp1 
            second = tmp2  
