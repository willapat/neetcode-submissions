# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #head points to the end
        #2 4 6 8 10
        #2 10 4 6 8
        #2 10 4 8 6
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        prev = None

        while mid:
            ahead = mid.next
            mid.next = prev
            prev = mid
            mid = ahead
        
        left = head
        while left and prev:
            l_ahead = left.next
            left.next = prev
            r_ahead = prev.next
            prev.next = l_ahead
            left = l_ahead
            prev = r_ahead
        


            
        

        
            
        

        
        
            
