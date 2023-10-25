def mergeTwoLists(self, list1, list2):
        output = ListNode()
        output.next = ListNode()
        output_head = output
        if list1==list2==None:
            return list1
        if list1==None:
            return list2
        if list2==None:
            return list1
        while list1!=None and list2!=None:
            print(list1.val,list2.val)
            if list1.val == list2.val:
                output.next = ListNode()
                output = output.next
                output.val = list1.val
                output.next = ListNode()
                output = output.next
                output.val = list2.val
                list1,list2 = list1.next, list2.next
            elif list1.val < list2.val:
                output.next = ListNode()
                output = output.next
                output.val = list1.val
                list1 = list1.next
            elif list1.val > list2.val:
                output.next = ListNode()
                output = output.next
                output.val = list2.val
                list2 = list2.next
        while list1!=None:
            output.next = ListNode()
            output = output.next
            output.val = list1.val
            list1 = list1.next
        while list2!=None:
            output.next = ListNode()
            output = output.next
            output.val = list2.val
            list2 = list2.next
        return output_head.next
