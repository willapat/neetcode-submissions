# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        #so we will merge like two at a time I guess
        for i in range(1, len(lists)):
            dummy = ListNode(0)
            curr = dummy
            while lists[i] and lists[i - 1]:
                if lists[i].val < lists[i - 1].val:
                    curr.next = lists[i]
                    lists[i] = lists[i].next
                    curr = curr.next
                else:
                    curr.next = lists[i - 1]
                    lists[i - 1] = lists[i - 1].next
                    curr = curr.next
            
            while lists[i]:
                curr.next = lists[i]
                lists[i] = lists[i].next
                curr = curr.next
            while lists[i - 1]:
                curr.next = lists[i - 1]
                lists[i - 1] = lists[i - 1].next
                curr = curr.next

            lists[i] = dummy.next
        
        return dummy.next
