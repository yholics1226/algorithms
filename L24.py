# [Swap Nodes in Pairs] https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        n1, n2 = head, head.next
        n1.next = self.swapPairs(n2.next)
        n2.next = n1
        return n2
