# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Floyd's Tortise and Hare Algo
        #Fast and Slow pointer, slow +1 and fast +2, if there is a cycle they will collide
        slow, fast = head, head
        while slow and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == None:
                return False
            elif slow == fast:
                return True
            
        return False
