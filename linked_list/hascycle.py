# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        length = 0
        while head!=None:
            head = head.next
            length += 1
            if length > 10000:
                return True
            
        return False