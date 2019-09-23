
class tree_node:
	def __init__ (self, val):
		self.v = val
		self.right = None
		self.left = None
		self.mark = 0

def insert(root, val):
	if root == None:
		root = tree_node(val)
	else:
		if val <= root.v:
			root.left = insert(root.left, val)
		else:
			root.right = insert(root.right, val)

	return root

def create_bst (val_list):
	root = None
	for i in range(0, len(val_list)):
		val = val_list[i]
		root = insert(root, val)

	return root

#pre_order DLR
#{{{
def pre_order_bst(root):
	total_list = []
	if root != None:
		total_list.append(root.v)
		total_list += pre_order_bst(root.left)
		total_list += pre_order_bst(root.right)
	return total_list

def DFS_pre_order_bst(root):
	stack = []
	total_list = []
	stack.append(root)
	while stack != []:
		this = stack[0]
		del(stack[0])

		if this.mark == 0:
			this.mark = 1
			if this.right != None:
				stack = [this.right] + stack
			if this.left != None:
				stack = [this.left] + stack
			stack = [this] + stack
		else:
			total_list.append(this.v)

	return total_list		
#}}}

#in_order LDR
#{{{
def in_order_bst(root):
	total_list = []
	if root != None:
		total_list += in_order_bst(root.left)
		total_list.append(root.v)
		total_list += in_order_bst(root.right)
	return total_list		

def DFS_in_order_bst(root):
	stack = []
	total_list = []
	stack.append(root)
	while stack != []:
		this = stack[0]
		del(stack[0])

		if this.mark == 0:
			this.mark = 1
			if this.right != None:
				stack = [this.right] + stack
			stack = [this] + stack
			if this.left != None:
				stack = [this.left] + stack
		else:
			total_list.append(this.v)

	return total_list		
#}}}

#post_order LRD
#{{{
def post_order_bst(root):
	total_list = []
	if root != None:
		total_list += post_order_bst(root.left)
		total_list += post_order_bst(root.right)
		total_list.append(root.v)
	return total_list		

def DFS_post_order_bst(root):
	stack = []
	total_list = []
	stack.append(root)
	while stack != []:
		this = stack[0]
		del(stack[0])

		if this.mark == 0:
			this.mark = 1
			stack = [this] + stack
			if this.right != None:
				stack = [this.right] + stack
			if this.left != None:
				stack = [this.left] + stack
		else:
			total_list.append(this.v)

	return total_list		
#}}}

#BFS
#{{{
def BFS_bst (root):
	fifo = []
	total_list = []
	fifo.append(root)
	while fifo != []:
		this = fifo[0]
		del(fifo[0])
		total_list.append(this.v)
		if this.left != None:
			fifo.append(this.left)
		if this.right != None:
			fifo.append(this.right)

	return total_list
#}}}


val_list = [2,3,1,9,5,6,7,4]


print "DLR"
tree_root = create_bst(val_list)
DLR_list = pre_order_bst(tree_root)
print DLR_list
DFS_DLR_list = DFS_pre_order_bst(tree_root)
print DFS_DLR_list

print "LDR"
tree_root = create_bst(val_list)
LDR_list = in_order_bst(tree_root)
print LDR_list
DFS_LDR_list = DFS_in_order_bst(tree_root)
print DFS_LDR_list

print "LRD"
tree_root = create_bst(val_list)
LRD_list = post_order_bst(tree_root)
print LRD_list
DFS_LRD_list = DFS_post_order_bst(tree_root)
print DFS_LRD_list

print "BFS"
BFS_list = BFS_bst(tree_root)
print BFS_list


