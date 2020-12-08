class bitree ():
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
        self.balance = 0
        
        self.is_avl = 1 
        

    def insert (self, value):
        #{{{
        val = self.value
        
        if value > val:
            if self.right == None:
                new = bitree(value)
                self.right = new
            else:
                self.right.insert(value)

        else:
            if self.left == None:
                new = bitree(value)
                self.left = new
            else:
                self.left.insert(value)
        self.update_height()
        if self.is_avl == 1:
            return self.self_balancing()
        else:
            return self
        #}}}

    def delete (self, value):
        #{{{
        #delete的办法有点费解，我的办法就是找到要删的点和它上面的点，以及上面点的左右信息，然后把这个要删的点一点一点下旋移动到叶子。同时还要保留它上面点的信息。
        #这个旋转过程要左右左右来保证不会出现balance大于2的情况。
        #当要删的点到叶子以后，删掉它，所谓的删掉就是把上面点的左或右指针变None。
        #当删完以后，这个树肯定不平了，就还要再让树做一次平衡。反正这个树不存在balance大于2的情况，肯定能平衡。
        p = self
        head = self
        sup_p = None
        sup_lr = None
        while True:
            if p.value == value:
                break
            elif p.value > value and p.left != None:
                sup_p = p
                sup_lr = "l"
                p = p.left
            elif p.value < value and p.right != None:
                sup_p = p
                sup_lr = "r"
                p = p.right
            else:
                #cannot find
                return head


        while p.left != None or p.right != None:
            if sup_p == None:
                #p is root
                rot_result = p.right_rotate()
                head = rot_result
                sup_p = head 
                sup_lr = "r"
                p = sup_p.right
            else:
                if sup_lr == "r":
                    rot_result = p.left_rotate()
                    sup_p.right = rot_result
                    sup_p = rot_result
                    sup_lr = "l"
                    p = sup_p.left
                elif sup_lr == "l":
                    rot_result = p.right_rotate()
                    sup_p.left = rot_result
                    sup_p = rot_result
                    sup_lr = "r"
                    p = sup_p.right



        if sup_lr == "l":
            sup_p.left = None
        elif sup_lr == "r":
            sup_p.right = None
   

        return head.self_balancing()
        #}}}

    def update_height(self):
        #{{{
        if self.right == None:
            right_height = 0
        else:
            self.right.update_height()
            right_height = self.right.height

        if self.left == None:
            left_height = 0
        else: 
            self.left.update_height()
            left_height = self.left.height

        self.height = max(left_height, right_height) + 1 
        self.balance = right_height - left_height
        #}}}
   
    def self_balancing (self):
        #{{{
        if self.balance == -2 and self.left.balance <= -1:
            #LL
            return self.right_rotate()
        elif self.balance == 2 and self.right.balance >= 1:
            #RR
            return self.left_rotate()
        elif self.balance == -2 and self.left.balance >= 1:
            #LR
            #left_rotate left, right_rotate self
            
            left_p = self.left
            self.left = left_p.left_rotate()
            return self.right_rotate()
        
        elif self.balance == 2 and self.right.balance <= -1:
            #RL
            #right_rotate right, left_rotate self
            
            right_p = self.right
            self.right = right_p.right_rotate()
            return self.left_rotate()
        else:
            return self
        #}}}

    def right_rotate (self):
        #{{{
        left_p = self.left        
        left_p_right = left_p.right

        self.left = left_p_right
        left_p.right = self   
        left_p.update_height()
        return left_p
        #}}}

    def left_rotate (self):
        #{{{
        right_p = self.right        
        right_p_left = right_p.left

        self.right = right_p_left
        right_p.left = self   
        right_p.update_height()
        return right_p
        #}}}








 
    def pre_traversal (self):
        #{{{
        result = []

        if self.left != None:
            result += self.left.pre_traversal()
        result += [self.value]        

        if self.right != None:
            result += self.right.pre_traversal()
        return result
        #}}}

    def in_traversal (self):
        #{{{
        result = []
        result += [self.value]        
        if self.left != None:
            result += self.left.in_traversal()

        if self.right != None:
            result += self.right.in_traversal()
        return result
        #}}}

    def post_traversal (self):
        #{{{
        result = []
        if self.left != None:
            result += self.left.post_traversal()

        if self.right != None:
            result += self.right.post_traversal()
        result += [self.value]        
        return result
        #}}}

    def level_traversal (self):
        #{{{
            this_fifo = []
            next_fifo = []
            this_fifo.append(self)
            while True:
                tmp = ""
                have_next = 0
                for node in this_fifo:
                    if node == None:
                        tmp += "None "
                        next_fifo.append(None)
                        next_fifo.append(None)
                        continue

                    tmp += str(node.value) + " "
                    next_fifo.append(node.left)
                    next_fifo.append(node.right)
                    if node.left != None or node.right != None:
                        have_next = 1
                print (tmp)
                if have_next == 0:
                    break
                this_fifo = next_fifo
                next_fifo = []
        #}}}

"""
head = bitree(60)
head.insert(40)
head.insert(70)
head.insert(20)
head.insert(50)
head.insert(45)
head.insert(51)

print ("height balance")
print (head.height)
print (head.balance)

print ("level traversal")
head.level_traversal()

head = head.self_balancing()
print ("height balance after balancing")
print (head.height)
print (head.balance)

print ("level traversal")
head.level_traversal()
"""

"""
head = bitree(60)
head.insert(40)
head.insert(70)
head.insert(65)
head.insert(75)
head.insert(63)
head.insert(66)

print ("height balance")
print (head.height)
print (head.balance)

print ("level traversal")
head.level_traversal()

head = head.self_balancing()
print ("height balance after balancing")
print (head.height)
print (head.balance)

print ("level traversal")
head.level_traversal()
"""

head = bitree(60)
head = head.insert(40)
head = head.insert(70)
head = head.insert(65)
head = head.insert(75)
head = head.insert(63)
head = head.insert(66)

print (head.height)
print (head.balance)
head.level_traversal()

head=head.delete(66)
#head = head.right_rotate()
head.level_traversal()

