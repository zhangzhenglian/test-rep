teachers=['A','B','C','D','E','F','G','H']
offices=[[],[],[]]
import random

for teacher in teachers:
    i=random.randint(0,2)
    offices[i].append(teacher)
j=1
for office in offices:
    num=len(office)
    print(f'办公室的{j}人数是{num},它们分别是：{office}')
    #for name in office:
        #print(name)
    j+=1






