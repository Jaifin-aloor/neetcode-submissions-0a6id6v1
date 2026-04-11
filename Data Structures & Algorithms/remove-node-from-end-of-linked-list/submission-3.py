# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return None

        node = head
        count, realcount = 0, 0
        while node:
            count += 1
            node = node.next
        todelete = count - n 

        if not todelete: return head.next

        node = head
        for i in range(todelete - 1):
            node = node.next
        node.next = node.next.next

        return head


        