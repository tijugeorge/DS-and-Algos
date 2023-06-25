class ListNode:
	def __init__(self, val):
		self.val = val 
		self.next = None 

one = ListNode(3)
two = ListNode(4)
three = ListNode(5)

one.next = two 
two.next = three 
head = one 


print(head.val)
print(head.next.next.val)

def get_sum(head):
	ans = 0
	while head:
		ans += head.val
		head = head.next 
	return ans 

def get_sumR(head):
	if head is None:
		return 0
	return head.val + get_sumR(head.next)

def add_node(prev_node, note_to_add):
	note_to_add.next = prev_node.next 
	prev_node.next = note_to_add
