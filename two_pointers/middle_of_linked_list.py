from linked_list import LinkedList

# The code in "linked_list.py" can be used to create a linked list out of a list. 
# The code in "linked_list_traversal.py" can be used to traverse the linked list.
# The code in "linked_list_reversal.py" can be used to reverse the linked list.

def get_middle_node(head):

    slow,fast = head,head

    while slow!= None and slow.next!=None and fast!=None and fast.next!=None:
        slow = slow.next
        if fast.next.next!=None:
            fast = fast.next.next
        else:
            return slow
    return slow

