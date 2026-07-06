# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find the middle most node of the linked list
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Disconnecting the Linked list
        second = slow.next
        slow.next = None

        # 3. Reverse the 2nd half of the linked list
        prev = None
        current = second
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        # 4. Merging the 2 linked list together
        first = head
        second = prev

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
