# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Step1: Find the middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        # Step2: Reverse the second half
        prev = None
        cur = slow.next
        slow.next = None

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        

        # Step 3: Merge the two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
