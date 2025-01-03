# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while slow!= None and fast!=None:
            if slow.next != None and fast.next != None and fast.next.next != None:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True
            else:
                return False 
        return False