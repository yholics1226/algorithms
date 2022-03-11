# [Rotate List] https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        ans = head
        n = 1
        while head.next:
            n += 1
            head = head.next
        head.next = ans
        for _ in range(n - k % n):
            head = head.next
        ans = head.next
        head.next = None
        return ans
