# 1.函数内部自己调用自己
# 2.要有出口，不然就呵呵了
def return_number(num):
    if num == 1:
        return 1
    return num + return_number(num - 1)


print(return_number(100))
