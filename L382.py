# [Linked List Random Node] https://leetcode.com/problems/linked-list-random-node/

import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self, head):
        self.vals = []
        while head:
            self.vals.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        idx = int(random.random() * len(self.vals))
        return self.vals[idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

# # To test on vscode? (printing form deformed)
# obj = Solution(ListNode(1, ListNode(2, ListNode(3))))
# print([obj.getRandom() for _ in range(5)])
