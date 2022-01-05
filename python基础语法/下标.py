str1 = 'abcdefg'
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[2:5])#默认左闭右开，步长为一
print(str1[2:5])#ctrl+d复制上一行
print(str1[2:5:2])
print(str1[2:5:2])
print(str1[:5])
print(str1[2:])
print(str1[:])
print(str1[-4:-1])
print(str1[-1:-4])#选取方向不一致，没有结果
print(str1[-1:-4:-1])#方向一致才能选取，-1到-4方向从左往右，步数-1也是往左选取
print(str1[::-1])#复数倒着取