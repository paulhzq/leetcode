# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        a = self
        while a.next != None:
            print(str(a.val))
            a = a.next
        print(str(a.val))

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    l1 and l2 may not have the same length, but either way the result will have at
    most n + 1 node.
    so we just iterate the l1,l2 and add the value, if the value >=10, make sure add the 1 to the next node.
    """
    rlist = ListNode(0)
    rlist_cp,l1_cp,l2_cp = rlist,l1,l2
    carry = 0
    while l1_cp != None or l2_cp != None:
        x1 = l1_cp.val if l1_cp != None else 0
        x2 = l2_cp.val if l2_cp != None else 0
        curVal = x1 + x2 + carry
        carry = 1 if curVal >=10 else 0
        rlist_cp.next = ListNode(curVal % 10)
        if(l1_cp != None):
            l1_cp = l1_cp.next
        if(l2_cp != None):
            l2_cp = l2_cp.next
        rlist_cp = rlist_cp.next
    if(carry>0):
        rlist_cp.next = ListNode(carry)
    return rlist.next

rlist = addTwoNumbers(ListNode(4),ListNode(8))
rlist.__str__()
