import os
flag=2
l = os.listdir()
print(l)
for i in l:
    if flag==1:
        newname = 'python_'+i
    elif flag==2:
        num=len('python_')
        newname=i[num:]
    os.rename(i, newname)
