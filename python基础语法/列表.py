name_list=['tom','lily','bose']
print(name_list[0])
print(name_list.index('tom',0,2))#index(数据,开始位置下标,结束位置下标)
print(name_list.count('tom'))
print(len(name_list))#列表中数据个数
print('tom'in name_list)#判断是否存在
print('tom'not in name_list)
'''
name=input('请输入您的用户名:')
if name in name_list:
    print('您输入的用户名已存在,请重新输入')
else:
    print(f"您输入的名字是{name},已完成注册,请稍等...")
'''
name_list.append('bob')  # 结尾追加数据
print(name_list)  # 列表可变
name_list.extend('xiaoming')  # 序列拆开加入
print(name_list)
name_list.extend(['xiaoming'])  # 列表不拆直接加入
print(name_list)
name_list.insert(0, 'jake')
print(name_list)
del name_list[0]
# del name_list全删
print(name_list)
name_list.pop(0)#如果不指定则默认删除最后一个
print(name_list)
name_list.remove('bob')
print(name_list)
name_list.clear()#清空列表,别忘记打()
name_list.append('error')
print(name_list)
name_list[0]='luncy'#修改指定位置数据
print(name_list)
list1=[1,9,3,6,5]
list1.reverse()#倒序排列
print(list1)
list1.sort(reverse=False)#升序
print(list1)
list1.sort(reverse=True)#降序
print(list1)
list1.sort()#默认升序
print(list1)