i = 1
result = 0
while i <= 100:
    result += i
    i = i + 1
print(result)

j = 0
result2 = 0
while j <= 100:
    result2 = result2 + j
    j = j + 2
print(result2)

a = 1
result3 = 0
while a <= 100:
    if a % 2 == 0:
        result3 += a
    a = a+1  #如果没打这行,赶紧停止运行,防止计算机卡死（下方红色方框）
print(result3)
