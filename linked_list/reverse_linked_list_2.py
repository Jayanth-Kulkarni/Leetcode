from linked_list import LinkedList
from linked_list_node import LinkedListNode
            
def reverse(head):

    prev,curr = None, head 

    while curr!=None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    return prev
