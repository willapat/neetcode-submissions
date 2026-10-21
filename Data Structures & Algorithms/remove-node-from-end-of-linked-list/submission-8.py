# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        target = length - n
        curr = head
        index = 1
        while curr and index < target:
            curr = curr.next
            index += 1
        
        if curr == head and target == 0:
            head = curr.next
        else:
            curr.next = curr.next.next
        
        return head