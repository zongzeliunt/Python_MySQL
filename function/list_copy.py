import copy

list_1 = [1,2,3]

list_2 = list_1
list_3 = copy.copy(list_1)
#python 3 can use list_1.copy()

del(list_2[2])

print list_1
print list_2
#both are [1,2], so list_2 is a pointer pointing to list_1

print list_3
#[1,2,3] list_3 is copied from list_1
