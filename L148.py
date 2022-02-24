# [Sort List] https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        tmp.sort()
        while tmp:
            head = ListNode(tmp.pop(), head)
        return head

# less memory
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head
        tmp = []
        while h:
            tmp.append(h.val)
            h = h.next
        tmp.sort()
        h = head
        for x in tmp:
            h.val = x
            h = h.next
        return head
