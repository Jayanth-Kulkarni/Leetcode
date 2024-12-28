# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        answer = ListNode()
        head = answer
        while list1!=None and list2!=None:
            if list1.val<=list2.val:
                answer.next = ListNode()
                answer.val = list1.val
                answer = answer.next
                list1 = list1.next
            elif list2.val<list1.val:
                answer.next = ListNode()
                answer.val = list2.val
                answer = answer.next
                list2 = list2.next
        if list1!=None:
            answer.val = list1.val
            answer.next = list1.next
        if list2!=None:
            answer.val = list2.val
            answer.next = list2.next

        
        return head
