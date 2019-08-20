#!/usr/bin/python
class tree_node:
    def __init__(self, val):
        print "init"
        self.data = val
        self.left = None
        self.right = None
        
    def show_data(self):
        print self.data
        print self.right
        print self.left

    def assign_data (self, val):
        self.data = val

    def insert(self, new_tree_node):
        if new_tree_node.data > self.data:
            if self.right == None:
                self.right = new_tree_node
            else:
                self.right.insert(new_tree_node)
        else:
            if self.left == None:
                self.left = new_tree_node
            else:
                self.left.insert(new_tree_node)

    def pre_order_travel (self):
        if not self.left == None:
            self.left.pre_order_travel()
        print self.data
        if not self.right == None:
            self.right.pre_order_travel()



number_list = [1,3,7,2,5,9,10,4]

root = tree_node(8)
root.show_data()

for num in number_list:
    print num
    a = tree_node(num)
    root.insert(a)

root.pre_order_travel()



