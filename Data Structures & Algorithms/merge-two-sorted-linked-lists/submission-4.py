# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        left = list1
        right = list2
        if left and right and left.val <= right.val:
            head = left
            left = left.next
        elif left and right:
            head = right
            right = right.next
        elif left:
            head = left
            left = left.next
        elif right:
            head = right
            right = right.next
        else:
            head = None
            return head

        curr = head
        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next

            curr = curr.next
        
        while left:
            curr.next = left
            left = left.next
            curr = curr.next
        
        while right:
            curr.next = right
            right = right.next
            curr = curr.next
        
        return head