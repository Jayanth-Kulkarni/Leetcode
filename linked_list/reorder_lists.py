# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# nums = [1,2,3,4,5]
# head = ListNode()
# question = head
# for idx,i in enumerate(nums):
# 	head.val = i
# 	if idx!=len(nums)-1:
# 		head.next = ListNode()
# 		head = head.next

list_mem = {}
i = 0 
head = question
while question:
	print(question.val)
	list_mem[i] = question
	i+=1
	question = question.next

reorder = []
for i,j in zip(range(0,len(list_mem)-1),range(len(list_mem)-1,0,-1)):
	if i not in reorder:
		reorder.append(i)
	if j not in reorder:
		reorder.append(j)

print(reorder)

res = head
for idx,i in enumerate(reorder[1:]):
	head.next = list_mem[i]
	print(idx,len(reorder)-2)
	if idx!=len(reorder)-2:
		head = head.next
	else:
		head.next.next = None

count = 0
while res and count<10:
	print(res.val)
	count +=1
	res = res.next