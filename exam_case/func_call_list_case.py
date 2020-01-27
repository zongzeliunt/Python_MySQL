#list 里可以存函数调用的引用，不直接调用函数，但是可以保存，到未来调用
#但是，在for结束后，i的内存已经已经被存入2了


list = []  
for i in range(3):  
    def test(x):
        print (i)
        print(x + i)

    list.append(test)  
print (list)
for num in list:  
    num(2)
