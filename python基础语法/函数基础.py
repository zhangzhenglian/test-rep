def add_num(a, b):
    result = a + b
    print(result)


add_num(10, 20)


def buy():
    return "烟"


'''return下方的函数体内部的代码不执行（退出当前代码）'''

goods = buy()
print(goods)


def num(a, b):
    '''
    求和函数
    :param a: 参数1
    :param b: 参数2
    :return: 返回值
    '''
    return a + b


print(num(1, 2))
help(num)


def testA():
    print('爱')


def testB():
    print('我')
    testA()
    print('你')


testB()  # 函数嵌套调用


def line():
    print("_" * 20)


line()


def lines(num):
    i = 0
    while i < num:
        print('-' * 20)
        i = i + 1


lines(5)


def sum_num(a, b, c):
    return a + b + c


print(sum_num(1, 2, 3))


def avage_num(a, b, c):
    result = sum_num(a, b, c)
    return result / 3


print(avage_num(3, 4, 5))


