class ListNode(object):

	def __init__(self, val, next=None):
		self.val = val
		self.next = next


class CrackingLinkedList(object):

	def print_list(self, head):
		cur = head
		while cur:
			print cur.val, '-->',
			cur = cur.next
		print 'None'

	def middle(self, head):
		if not head:
			return None
		slow, fast = head, head
		while fast.next and fast.next.next:
			fast = fast.next.next
			slow = slow.next
		return slow

	def remove_dups_unsorted(self, head):
		if not head:
			return None
		prev, cur, map = None, head, set()
		while cur:
			if cur.val not in map:
				map.add(cur.val)
				prev = cur
			else:
				prev.next = cur.next
			cur = cur.next	
		return head

	def remove_dups_unsorted2(self, head):
		if not head:
			return None
		marker = head
		while marker:
			prev, cur = marker, marker.next
			while cur:
				if cur.val == marker.val:
					prev.next = cur.next
				else:
					prev = cur
				cur = cur.next
			marker = marker.next
		return head

	def remove_dups_unsorted3(self, head):
		if not head:
			return None
		head = self.merge_sort(head)
		return self.remove_dups_sorted(head)

	def merge_sort(self, head):
		pass

	def merge_two_sorted(self, l1, l2):
		pass
		
	def remove_dups_sorted(self, head):
		if not head:
			return None
		prev, cur = head, head.next
		while cur:
			if cur.val == prev.val:
				prev.next = cur.next
			else:
				prev = cur
			cur = cur.next
		return head

	
def main():
	cc = CrackingLinkedList()
	print 'List1: '
	node4 = ListNode(0)
	node3 = ListNode(3, node4)
	node2 = ListNode(0, node3)
	node1 = ListNode(0, node2)
	head = ListNode(0, node1)
	cc.print_list(head)

	print 'rm dups:'	
	cc.print_list(cc.remove_dups_unsorted(head))
	cc.print_list(cc.remove_dups_unsorted2(head))
	print

	print 'List2: '
	node4 = ListNode(3)
	# node3 = ListNode(3, node4)
	node2 = ListNode(2, node4)
	node1 = ListNode(1, node2)
	head = ListNode(0, node1)
	cc.print_list(head)
	
	print 'rm dups:'	
	cc.print_list(cc.remove_dups_unsorted(head))
	cc.print_list(cc.remove_dups_unsorted2(head))
	cc.print_list(cc.remove_dups_sorted(head))
	print 

	print 'List3: '
	node1 = ListNode(0, node2)
	head = ListNode(0, node1)
	cc.print_list(head)
	
	print 'rm dups:'	
	cc.print_list(cc.remove_dups_unsorted(head))
	cc.print_list(cc.remove_dups_unsorted2(head))

if __name__ == '__main__':
	main()
