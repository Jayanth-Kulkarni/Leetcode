class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        if head == None:
            return head
        while head:
            stack.append(head.val)
            head = head.next

        output = ListNode()
        output_head = output
        while len(stack) != 0:
            output.val = stack.pop()
            # print(output.val)
            if len(stack) != 0:
                output.next = ListNode()
                output = output.next
        return output_head