"""
Leetcode 21
Merge Two Sorted Lists
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        p1 = list1
        p2 = list2
        curr = dummy = ListNode()
        
        while p1 and p2:           
            if p1.val <= p2.val: 
                curr.next = p1
                p1 = p1.next
            else: 
                curr.next = p2
                p2 = p2.next
            
            curr = curr.next
         
        if p1: 
            curr.next = p1
        else: 
            curr.next = p2
        
        return dummy.next