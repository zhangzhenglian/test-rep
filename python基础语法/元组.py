t1 = (10,20,30)#元组不可更改
print(t1)
print(type(t1))#tuple
t2=(10,)
print(type(t2))#typle
t3=(10)#元组必须加逗号
print(type(t3))#int
t4 = ('aaa')
print(type(t4))#str
#元组只支持查找
print(t1[0])
print(t1.index(10))
print(t1.count(10))
print(len(t1))
t5=(10,20,['aa','bb'])
t5[2][0]='tom'
print(t5)
