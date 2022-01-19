# [Linked List Cycle 2] https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        tmp = head
        while tmp:
            if tmp in seen:
                return tmp
            else:
                seen.add(tmp)
                tmp = tmp.next
        return None

# another solution
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        while fast != head:
            fast = fast.next
            head = head.next
        return fast
