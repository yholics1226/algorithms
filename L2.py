# [Add Two Numbers] https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = node = ListNode()
        over = 0
        while l1 or l2 or over:
            node.next = ListNode()
            node = node.next
            if l1: 
                over += l1.val
                l1 = l1.next
            if l2: 
                over += l2.val
                l2 = l2.next
            over, node.val = divmod(over, 10)
        return ans.next
