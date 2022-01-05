# abs求绝对值
# round四舍五入
print(abs(-10))
print(round(1.2))
print(round(1.7))


def sum_num(a, b, f):
    return f(a) + f(b)


print(sum_num(-1, 1, abs))
print(sum_num(1.9, 2.1, round))  # 函数作为参数进行使用，起到了简化代码的作用，这就是高阶函数
# map将函数作用到列表中的每一个元素
list1 = [1, 2, 3, 4, 5]


def func(x):
    return x ** 2


result = map(func, list1)
print(result)  # 不显示结果，只显示 存储位置
print(list(result))  # 将结果转换成列表list（），并打印列表
# reduce作用：功能函数计算的结果作为a下一个数据作为b继续运算
import functools  # 导入模块reduce函数在functools模块中，不导入则无法使用


def func2(a, b):
    return a + b


def func3(a, b):
    return a * b


result2 = functools.reduce(func2, list1)  # reduce里的func函数必须包含两个参数，否则程序无法运行
result3 = functools.reduce(func3, list1)  # reduce里的func函数必须包含两个参数，否则程序无法运行
print(result2, result3)


# filter(func,list)过滤不符合条件的函数
def func4(x):
    return x % 2 == 0


result4 = filter(func4, list1)
print(list(result4))
