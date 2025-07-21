class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorders a linked list from:
        L0 → L1 → L2 → ... → Ln-1 → Ln
        to:
        L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

        Modifies the list in-place.
        """

        if not head or not head.next:
            return

        # Step 1: Find the middle of the linked list
        slow_ptr = fast_ptr = head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        # Step 2: Reverse the second half of the list
        prev_node = None
        curr_node = slow_ptr.next
        slow_ptr.next = None  # Cut the list in half

        while curr_node:
            next_temp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_temp

        # prev_node now points to the head of reversed second half

        # Step 3: Merge the two halves alternately
        first_half_ptr = head
        second_half_ptr = prev_node

        while second_half_ptr:
            temp1 = first_half_ptr.next
            temp2 = second_half_ptr.next

            first_half_ptr.next = second_half_ptr
            second_half_ptr.next = temp1

            first_half_ptr = temp1
            second_half_ptr = temp2
