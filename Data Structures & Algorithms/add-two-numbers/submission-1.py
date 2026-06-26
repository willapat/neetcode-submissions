# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = 0
        multiplier = 1
        left, right = l1, l2
        while left and right:
            sum += left.val * multiplier
            sum += right.val * multiplier
            left = left.next
            right = right.next
            multiplier *= 10
        
        while left:
            sum += left.val * multiplier
            left = left.next
            multiplier *= 10

        while right:
            sum += right.val * multiplier
            right = right.next
            multiplier *= 10
        
        #need go from ones to however big the number is
        # 975 mod 10 divide by 1 gives 5
        # 975 mod 100 divided by 10 gives 7
        # 975 mod 1000 divided by 100 gives 9
        val = (sum % 10) // 1
        sum -= val
        head = ListNode(val)
        mod, divide = 100, 10
        curr = head
        while sum > 0:
            val = (sum % mod) // divide
            sum -= val * divide
            mod *= 10
            divide *= 10
            node = ListNode(val)
            curr.next = node
            curr = node
        
        return head
        
