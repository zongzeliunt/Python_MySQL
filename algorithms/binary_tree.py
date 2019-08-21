#!/usr/bin/python


class node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.v = val
		self.mark = 0

def node_insert (root, val):
	root_val = root.v
	if val < root_val:
		if root.left == None:
			new_node = node(val)
			root.left = new_node
		else:
			node_insert(root.left, val)
	else:
		if root.right == None:
			new_node = node(val)
			root.right = new_node
		else:
			node_insert(root.right, val)

#in_order
#{{{
def in_order_search (root):
	if not root.left == None:
		in_order_search (root.left)
	print root.v
	if not root.right == None:
		in_order_search (root.right)


def LDR (root):
	stack = [root]
	while not len(stack) == 0:
		current = stack[0]
		del(stack[0])
		if current.mark == 0:
			if not current.right == None:
				stack = [current.right] + stack
			current.mark = 1	
			stack = [current] + stack
			if not current.left == None:
				stack = [current.left] + stack
		else:
			print current.v

	"""
	stack = []
	current = root
	while True:
		while not current == None:
			stack = [current] + stack
			current = current.left
		if not len(stack) == 0:
			current = stack[0]
			del(stack[0])
			print current.v
			current = current.right

		if current == None and len(stack) == 0:
			break
	"""
#}}}

#pre_order
#{{{
def pre_order_search (root):
	print root.v
	if not root.left == None:
		pre_order_search (root.left)
	if not root.right == None:
		pre_order_search (root.right)

def DLR (root):
	stack = [root]
	while not len(stack) == 0:
		current = stack[0]
		del(stack[0])
		if current.mark == 0:
			if not current.right == None:
				stack = [current.right] + stack
			if not current.left == None:
				stack = [current.left] + stack
			current.mark = 1	
			stack = [current] + stack
		else:
			print current.v

	"""
	stack = [root] + stack

	while not len(stack) == 0:
		current = stack[0]
		print current.v
		del (stack[0])
		if not current.right == None:
			stack = [current.right] + stack
		if not current.left == None:
			stack = [current.left] + stack
	"""
#}}}

#post_order
#{{{
def post_order_search (root):
	if not root.left == None:
		post_order_search (root.left)
	if not root.right == None:
		post_order_search (root.right)
	print root.v

def LRD (root):
	stack = [root]
	while not len(stack) == 0:
		current = stack[0]
		del(stack[0])
		if current.mark == 0:
			current.mark = 1	
			stack = [current] + stack
			if not current.right == None:
				stack = [current.right] + stack
			if not current.left == None:
				stack = [current.left] + stack
		else:
			print current.v

	"""
	stack = []
	current = root
	r_push_list = []
	while True:
		if not current == None:
			stack = [current] + stack
			current = current.left
		else:
			current = stack[0] 
			if current in r_push_list:
				print current.v
				del(stack[0])
				current = None
			else:
				r_push_list.append(current) 
				current = current.right

		if current == None and len(stack) == 0:
			break
	"""

#}}}

def breadth_first_search (root):
#{{{
	queue = []
	queue.append([root, 0])
	report_tmp = ""
	report_level = 0
	while not queue == []:
		this = queue[0]
		del(queue[0])
		this_node = this[0]
		this_level = this[1]
		if this_level == report_level:
			report_tmp += str(this_node.v) + " "
		else:
			print "level: " + str(report_level) + ": " + report_tmp
			report_tmp = ""
			report_level += 1
			report_tmp += str(this_node.v) + " "
		if not this_node.left == None:
			queue.append([this_node.left, this_level + 1])
		if not this_node.right == None:
			queue.append([this_node.right, this_level + 1])


	if not report_tmp == "":
		print "level: " + str(report_level) + ": " + report_tmp
#}}}

#AVL tree
#	find_tree_depth
#	rotate_right
#	rotate_left
#	AVL_tree_balance
#{{{
def find_tree_depth (root):
	if root == None:
		return 0
	
	left_depth = find_tree_depth(root.left)
	right_depth = find_tree_depth(root.right)

	return max(left_depth, right_depth) + 1


def rotate_right (root):
	left = root.left
	right = root.right
	root.left = left.right
	left.right = root
	root = left
	return root

def rotate_left (root):
	left = root.left
	right = root.right
	
	root.right = right.left
	right.left = root
	root = right
	return root

def AVL_tree_balance (root):
	unbalance = 1
	while unbalance == 1:
		left_depth = find_tree_depth (root.left)
		right_depth = find_tree_depth (root.right)
		if abs(left_depth - right_depth) <= 1:
			#unbalance
			unbalance = 0
			break
		if left_depth > right_depth:
			root = rotate_right (root)
		else:
			root = rotate_left (root)
		breadth_first_search (root)
#}}}

def main ():
	num_list = [3,2,5,10,4,1,6,9,11,8,12]
	#num_list = [2,3,4,5]
	root = node(7)
	for num in num_list:
		node_insert(root, num)

	#print "tree_depth: " + str(find_tree_depth(root))
	#AVL_tree_balance(root)

	"""
	breadth_first_search (root)
	print "recursive:"
	in_order_search(root)
	print "LDR"
	LDR(root)
	"""	
	"""
	print "recursive:"
	pre_order_search(root)
	print "DLR"
	DLR(root)
	"""
	print "recursive:"
	post_order_search(root)
	print "LRD"
	LRD(root)




		
main()

