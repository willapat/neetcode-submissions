"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {}
        curr = head
        while curr:
            mp[curr] = Node(curr.val)
            curr = curr.next
        #all new nodes are stored

        mp[None] = None
        curr = head
        while curr:
            mp[curr].random = mp[curr.random]
            mp[curr].next = mp[curr.next]
            curr = curr.next

        return mp[head]
