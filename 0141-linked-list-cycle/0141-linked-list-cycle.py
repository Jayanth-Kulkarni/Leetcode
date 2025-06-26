# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        have 2 pointers, 1 moving at twice the speed as the other
        see if they meet, if yes return true; otherwise false
        """
        slow, fast = head, head
        while slow and slow.next and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False