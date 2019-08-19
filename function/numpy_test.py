import copy, numpy as np

a = np.zeros ((2,3), int)
b = np.zeros ((2,3), int)

print "initial a"
print a
print "initial b"
print b
print "type of a"
print type(a)

#a[0] = [1,2,3]
#a[1] = [4,5,6]
a[:][:] = [[1,2,3],[4,5,6]]
b[:][:] = [[7,8,9],[10,11,12]]

print "a with value"
print a
print "b with value"
print b

c = a + b
print "c = a + b"
print c
d = a*b
print "d = a * b"
print d

g= a.dot(b.T)
print "g = a.dot(b.T)"
print g

print "==================================="
print "second test"
a = np.zeros( (1,3), int)
a[0] = [1,2,3]

b = np.zeros( (1,3), int)
b[0] = [4,5,6]

print "a with value"
print a
print "b with value"
print b

c = a+ b
print "c = a + b"
print c

d = a*b
print "d = a * b"
print d

e = a.T * b
print "e = a.T * b" 
print e

f = a * b.T
print "f = a * b.T"
print f

g= a.dot(b.T)
print "g = a.dot(b.T)"
print g
