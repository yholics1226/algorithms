# [Reverse Linked List II] https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        ans = prev = ListNode()
        prev.next = head
        for _ in range(left - 1):
            prev = prev.next
        cur = prev.next
        nxt = cur.next
        for _ in range(right - left):
            x, y = prev.next, nxt.next
            prev.next = nxt
            nxt.next, cur.next = x, y
            nxt = y
        return ans.next
