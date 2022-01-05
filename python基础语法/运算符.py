# + * 支持列表，元组,字符串
list1=[10,20]
list2=[40,20,50,80]
dict1={'name':'python'}
print(list1+list2)
print(list1*5)#起复制作用
#in,not in 判断是否存在,支持字典
print('s'in list1)
print(len(list1))#统计容器中元素个数
del list1[0]
print(list1)
print(max(list2))
print(min(list2))
for i in range(1,10,2):
    print(i)
for j in range(10):
    print(j)
#enumerate 列举，计算
for i in enumerate(list2,start=0):
    print(i)
#tuple元组，list列表，set集合
print(tuple(list2))
print(list(dict1))
print(set(list2))
