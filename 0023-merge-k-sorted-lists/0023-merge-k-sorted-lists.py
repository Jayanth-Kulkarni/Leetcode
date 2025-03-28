# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergelists = []
            for i in range(0, len(lists), 2):
                l1, l2 = lists[i], lists[i+1] if i+1 < len(lists) else None
                mergelists.append(self.merge(l1, l2))
            lists = mergelists
        return lists[0]
    
    def merge(self, l1, l2):
        head = ListNode()
        tail = head

        while l1 and l2:
            if l1.val >= l2.val:
                tail.next = l2
                l2 = l2.next
            elif l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        
        if l2:
            tail.next = l2
        
        return head.next