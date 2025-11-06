# 2. Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are 
# stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and 
# return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# https://leetcode.com/problems/add-two-numbers

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # O(max(m,n))
        tmp = ListNode()
        tail = tmp
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            total = v1 + v2 + carry
            carry = total // 10
            
            tail.next = ListNode(val=total % 10)
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return tmp.next
