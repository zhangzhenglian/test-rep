def test1():
    a = 100
    print(a)


test1()
# print(a)报错这里a属于局部变量，临时储存在函数中
a = 100


def test2():
    print(a)


test2()
print(a)


# print(a)不报错这里a属于全局变量，没有储存在函数中
def test3():
    global a  # 强调修改a为全局变量
    a = 200
    print(a)


test3()  # 如果不调用函数结果仍为原来的a
print(a)


def test4():
    return 101


def test5(num):
    print(num)


num = test4()
test5(num)  # 返回值作为参数传递


def link():
    return 1, 2  # 默认返回元组


print(link())


def link1():
    return [1, 2]


print(link1())


def link3():
    return {1, 2}


print(link3())


def user_info(name, age, gender):
    print(f'姓名{name}，年龄{age}，性别{gender}')


user_info('张政连', 20, '男')
user_info(age=20, gender='男', name='张政连')


# user_info(age=20, gender='男', '张政连')位置参数必须放在关键字参数前，否则报错。
def user_info(name, age, gender='男'):
    print(f'姓名{name}，年龄{age}，性别{gender}')


# user_info('张政连', 20, '女')修改默认值
user_info('张政连', 20, )  # 不输入则默认


def p(*args):  # 不定长，将参数打包成元组
    print(args)


p('tom', 20)
p()  # 不输入也可以


def pa(**kwargs):
    print(kwargs)


pa(name='tom', age=20, id=1)  # 返回字典


def return_num():
    return 100, 200


num1, num2 = return_num()  # 拆包
print(num1, num2)
dict1 = {'name': 'tom', 'age': 20}
a, b = dict  # 字典拆包
print(a)
print(b)
print(dict1[a])
print(dict1[b])
a, b = 1, 2
b, a = a, b
print(a)
print(b)
a = b
print(id(a))
print(id(b))
b = 2
print(a)
print(id(a))
print(id(b))
aa = [10, 20]
bb = aa
print(id(aa))
print(id(bb))
aa.append(30)  # 列表可变
print(bb)
print(id(aa))
print(id(bb))


def test6(a):
    print(a)


a = 100
b = [100, 200]
test6(a)
test6(b)  # 引用可以当作实参传入
# 列表，字典，集合属于可变类型
