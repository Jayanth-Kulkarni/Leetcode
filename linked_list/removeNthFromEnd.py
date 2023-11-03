# Definition for singly-linked list.
# Edge cases: 
    # 1. when the first element is removed, just return head.next
    # 2. when there is only 1 element in the linkedlist and it has to be removed, return none  
# 0. Save the head as a pointer variable, save it before each pass 
# 1. Do 1 pass and get the length of linked list
# 2. Find the index number corresponding to the nth node from the end
# 3. Do another pass and make the next of n-1th node as n+1th node
# 4. Return the head pointer


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


nums = [1,2,3,4,5]
nums = [1]
nums = [1,2]
head = ListNode()
question = head
for idx,i in enumerate(nums):
  head.val = i
  if idx!=len(nums)-1:
      head.next = ListNode()
      head = head.next

class Solution:
    def removeNthFromEnd(self, head, n):
        question = head
        head_len = 0
        while head!=None:
            head_len+=1
            head = head.next
        # print(head_len)

        head = question
        target = head_len-n
        target_count = 0
        if head_len ==1 and n==1:
            return None
        if target==0:
            return head.next
        # print("target = ",target)
        while head!=None:
            # print(head.val,target_count)
            if target_count==target-1:
                # print("found target's left",head.val)
                head.next = head.next.next
            head = head.next
            target_count+=1

        return question

s = Solution()
s.removeNthFromEnd(question,2)