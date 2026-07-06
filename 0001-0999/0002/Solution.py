"""
@author Stellagosa
@description 2.两数相加
@date 7/6/2026 1:33 PM Monday
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
        temp = 0
        res = ListNode(0)
        node = res
        while l1 is not None or l2 is not None or temp != 0:
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            s = v1 + v2 + temp
            node.next = ListNode(s % 10)
            node = node.next
            temp = s // 10

        return res.next
