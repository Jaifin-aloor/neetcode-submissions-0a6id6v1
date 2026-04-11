# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = n2 = ""
        cur = l1
        while cur:
            n1 += str(cur.val)
            cur = cur.next
        
        cur = l2
        while cur:
            n2 += str(cur.val)
            cur = cur.next
        
        n1, n2 = int(n1[::-1]), int(n2[::-1])

        n3 = str(n1 + n2)[::-1]

        head = ListNode(int())
        cur = head
        for i in range(len(n3)):
            cur.val = int(n3[i])
            if i < len(n3) - 1:
                cur.next = ListNode()
                cur = cur.next

        return head



        