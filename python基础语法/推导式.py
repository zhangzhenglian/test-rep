list1=[]
i=0
while i <10:
    list1.append(i)
    i+=1
print(list1)
for i in range(10):
    list1.append(i)
print(list1)
list2=[i for i in range(10)]
print(list2)
list3=[i for i in range(10) if i%2==0]
print(list3)
list4=[(i,j) for i in range(1,3) for j in range(3)]
print(list4)
list5=[]
for i in range(1,3):
    for j in range(3):
        list5.append((i,j))
print(list5)
dict1={i:i**2 for i in range(1,5)}
print(dict1)
list6=['name','age','gender']
list7=['TOM','20','man']
dict2={list6[i]:list7[i] for i in range(len(list6))}#列表个数不同，统计多数列表报错，少的不报错
print(dict2)
counts={'a':263,'b':103,'c':201,'d':199}
count1={key: value for key,value in counts.items() if value>=200 }
print(count1)