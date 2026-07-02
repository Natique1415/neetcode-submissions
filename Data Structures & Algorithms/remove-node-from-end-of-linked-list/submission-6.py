# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        else:
            # finding the length of the list
            current, l = head, 0
            while current is not None:
                l += 1
                current = current.next

            # something to do with head
            if l == n:
                head = head.next
                return head

            # not do with head
            else:
                # go to the one node before the actual node to be deleted
                current = head
                l = l - n
                while l > 1:
                    l -= 1
                    current = current.next

                current.next = current.next.next
                return head
