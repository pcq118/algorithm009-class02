# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        thead = ListNode(-1)
        head = thead
        thead.next = l1
        while l1!=None  and l2!=None:
            if l1.val < l2.val:
                thead.next = l1
                l1 = l1.next
            else:
                thead.next = l2
                l2 = l2.next
            thead = thead.next
        thead.next = l1 if l2 == None else l2 
        return head.next