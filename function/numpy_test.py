import copy, numpy as np

print ("===================================")
print ("zero test, np array")
#{{{
a = np.zeros ((2,3), int)
b = np.zeros_like (a)

print ("initial a")
print (a)
print ("initial b")
print (b)
print ("type of a")
print (type(a))
print ("size of a")
print (a.size)
print ("shape of a")
print (a.shape)

#a[:][:] = [[1,2,3],[4,5,6]]

print ("random whole a, assign whole b, assign a[0]")
a = np.random.randint(10, size = a.shape)
a[0] = [1,2,3]
b[:][:] = [[7,8,9],[10,11,12]]

print ("a value")
print (a)
print ("b value")
print (b)
#}}}

"""
print ("===================================")
print ("first test, basic operations")
#{{{
c = a + b
print ("c = a + b")
print (c)
d = a*b
print ("d = a * b")
print (d)

e = a.dot(b.T)
print ("e = a.dot(b.T)")
print (e)

f = a.T.dot(b)
print ("f = a.T.dot(b)")
print (f)
#}}}
"""

"""
print ("===================================")
print ("second test, tile 就是同一个矩阵复制")
#{{{
b = np.tile(a, 2)
print ("a tile 2")
print (b)

c = np.tile(a, (2,2))
print ("a tile 2 * 2")
print (c)

d = np.tile(a, (2,1))
print ("a tile 1 * 2")
print (d)
#}}}
"""

print ("===================================")
print ("third test, nonzero")
#{{{
x = np.array([[3, 0, 0], [0, 4, 0], [5, 6, 7]])
b = np.nonzero(x)
print(np.array(b).ndim)
    #2
print(b)
    #(array([0, 1, 2, 2, 2]), array([0, 1, 0, 1, 2]))
    #即，(0，0),(1,1),(2,0),(2,1),(2,2) 诡异的排列法
    #但是其实这么排出来也是有道理，因为x可能是个多维的数组，b 的ndim就是把这个维告诉你，然后按每一维为单位打出非0的数的坐标。

print(np.transpose(np.nonzero(x)))


#}}}

print ("===================================")
print ("third test, random")
#{{{




#}}}
