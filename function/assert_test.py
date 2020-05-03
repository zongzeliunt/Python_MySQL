#^函数是异或，相同为0不同为1
def fulladder(A, B, C):
    return A^B^C, A&B|B&C|C&A # sum, carry

#assert 的意义就是如果是判断为真就执行后面的操作

assert fulladder(1, 0, 0) == (1, 0), "Failed"
assert fulladder(0, 1, 0) == (1, 0), "Failed"
assert fulladder(1, 1, 0) == (0, 1), "Failed"
assert fulladder(1, 0, 1) == (0, 1), "Failed"
assert fulladder(1, 1, 1) == (1, 1), "Failed"

print("Success!")
