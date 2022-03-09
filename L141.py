# [Linked List Cycle] https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# another solution
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.val == 1000000:
                return True
            head.val = 1000000
            head = head.next
        return False

# another solution
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        tmp = head
        while tmp:
            if tmp in seen:
                return True
            else:
                seen.add(tmp)
                tmp = tmp.next
        return False
