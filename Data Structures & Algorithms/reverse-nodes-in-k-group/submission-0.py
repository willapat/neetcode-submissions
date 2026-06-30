# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, node, nxt):
        curr = node
        prev = nxt
        while curr and curr != nxt:
            ahead = curr.next
            curr.next = prev
            prev = curr
            curr = ahead
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # find the k-th node ahead of groupPrev
            kth = groupPrev
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # fewer than k nodes left, stop here

            groupNext = kth.next         # node right after this group
            groupTail = groupPrev.next   # current head of group -> becomes tail after reversal

            newHead = self.reverse(groupTail, groupNext)

            groupPrev.next = newHead     # link previous group to new head
            groupPrev = groupTail        # old head is now tail; it's the new groupPrev

        return dummy.next

        

    
