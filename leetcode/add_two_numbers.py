# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = head = None
        carry = 0
        while l1 or l2:

            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0
            new_value = v1 + v2 + carry

            if new_value < 10:
                carry = 0
            else:
                carry = 1
                new_value = new_value % 10

            new_node = ListNode(new_value)

            if head is None:
                curr = head = new_node

            else:
                curr.next = new_node
                curr = new_node

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

            if not l1 and not l2 and carry:
                new_node = ListNode(carry)
                curr.next = new_node

        return head





