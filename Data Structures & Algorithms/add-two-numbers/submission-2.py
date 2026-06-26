# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        left, right = l1, l2
        dummy = ListNode()
        curr = dummy
        while left or right or carry:
            l = left.val if left else 0
            r = right.val if right else 0
            
            total = r + l + carry
            carry = total // 10
            total = total % 10
            curr.next = ListNode(total)

            curr = curr.next
            
            if left != None:
                left = left.next
            else:
                left = None
            if right != None:
                right = right.next
            else:
                right = None
        return dummy.next
            
            