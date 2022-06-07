# [Intersection of Two Linked Lists] https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s = set()
        while headA:
            s.add(headA)
            headA = headA.next
        while headB:
            if headB in s:
                return headB
            headB = headB.next
        return None

# another solution
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        x, y = headA, headB
        while x != y:
            x = x.next if x else headB
            y = y.next if y else headA
        return x
