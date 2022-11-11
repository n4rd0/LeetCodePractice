# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        print(list1.val, list2.val)
        head = sorted_list = ListNode()
        while (list1 and list2):
                
            if list1.val < list2.val:
                sorted_list.next = list1
                list1 = list1.next
                sorted_list = sorted_list.next

            elif list1.val >= list2.val:
                sorted_list.next = list2
                list2 = list2.next
                sorted_list = sorted_list.next
                
        sorted_list.next = list1 or list2
        return head.next()

sol = Solution()

print(sol.mergeTwoLists([1,2,4,7], [1,3,4]))