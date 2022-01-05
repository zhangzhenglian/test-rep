fn1 = lambda: 100
print(fn1)  # 存储位置
print(fn1())  # 存储值


def add(a, b):
    return a + b


result = add(1, 2)
print(result)
fn2 = lambda c, d: c + d
print(fn2(2,3))
fn3=lambda a:a
print(fn3('hello world'))
fn4=lambda a,b,c=100:a+b+c
print(fn4(10,20))
fn5=lambda *args:args
print(fn5(10,20,30))#可变参数返回元组
fn6=lambda **kwargs:kwargs
print(fn6(name='python',age='20'))#可变参数返回字典
fn7=lambda a,b:a if a>b else b
print(fn7(1000,999))#工作案例
students=[{'name':'TOM','age':20},{'name':'ROSE','age':19},{'name':'BOB','age':22}]
students.sort(key=lambda x:x['name'])
print(students)
students.sort(key=lambda x:x['name'],reverse=True)
print(students)
students.sort(key=lambda x:x['age'],reverse=True)
print(students)
students.sort(key=lambda x:x['age'])
print(students)