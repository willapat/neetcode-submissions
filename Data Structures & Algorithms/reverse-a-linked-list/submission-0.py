# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0 1 2 3
        # we want 1 to point at 0, and 0 to point at None, and 2 to point at 1
        curr = head
        prev = None


        while curr:
            ahead = curr.next
            curr.next = prev
            prev = curr
            curr = ahead

        
        head = prev

        return head