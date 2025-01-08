# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == list2 == None:
            return None
        
        result = ListNode()
        head = result
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                result.val = list1.val
                result.next = ListNode()
                result = result.next
                list1 = list1.next
            else:
                result.val = list2.val
                result.next = ListNode()
                result = result.next
                list2 = list2.next
        
        if list1 != None:
            result.val = list1.val
            result.next = list1.next
        
        if list2 != None:
            result.val = list2.val
            result.next = list2.next
            
        return head