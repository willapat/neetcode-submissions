# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr.next:
            greatCom = math.gcd(curr.val, curr.next.val)
            nextNode = curr.next
            curr.next = ListNode(greatCom)
            curr.next.next = nextNode
            curr = curr.next.next
        
        return head