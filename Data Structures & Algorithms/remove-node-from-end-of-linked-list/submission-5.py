# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            head = None
            return head
        
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        index = n % length
        i = length
        curr = head
        while i != index + 1:
            i -= 1
            curr = curr.next
        
        if curr.next == None:
            removed = head
            head = head.next
        else:
            removed = curr.next
            curr.next = curr.next.next

        if removed == head:
            return head.next
        return head