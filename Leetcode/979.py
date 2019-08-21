
class node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.v = val

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



def convert_list_to_tree (a):
#{{{
    root = node(a[0])
    queue = [root]
    i = 1 

    while i < len(a):  
        this_node = queue[0]
        del(queue[0])
        
        this_num = a[i]
        if not this_num == "null":
            new_node = node(this_num)        
            this_node.left = new_node
            queue.append(new_node)

        i += 1
        if i == len(a):
            break
        
        this_num = a[i]
        if not this_num == "null":
            new_node = node(this_num)        
            this_node.right = new_node
            queue.append(new_node)
        i += 1

    return root
#}}}

def move_coin (root):
    if root == None:
        return 0, 0
    
    left_need_count, left_move_count = move_coin(root.left)
    right_need_count, right_move_count = move_coin(root.right)

    total_need_count = left_need_count + right_need_count + root.v - 1
    total_move_count = left_move_count + right_move_count

    if total_need_count < 0:
        total_move_count += total_need_count * (-1)
    else:
        total_move_count += total_need_count

    print "v " + str(root.v)
    print "need " + str(total_need_count - 1)
    print "move " + str(total_move_count)


    return total_need_count , total_move_count





a = [1,0,0,"null",3]

root = convert_list_to_tree(a)
breadth_first_search(root)

need_count, move_count = move_coin(root)
print need_count
print move_count




    """
    def distributeCoins(self, root):
        def move_coin (root):
            if root == None:
                return 0, 0
    
            left_need_count, left_move_count = move_coin(root.left)
            right_need_count, right_move_count = move_coin(root.right)

            total_need_count = left_need_count + right_need_count + root.val - 1
            total_move_count = left_move_count + right_move_count

            if total_need_count < 0:
                total_move_count += total_need_count * (-1)
            else:
                total_move_count += total_need_count


            return total_need_count , total_move_count
        
        
        
        need_count, move_count = move_coin(root)
        return move_count
    """
