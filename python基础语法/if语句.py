age = 20
if age >= 18:
    print("可以上网")
if age < 18:
    print("不可上网")
age = int(input('请输入您的年龄：'))#int转换数据类型不要忘
if age >= 18:
    print("可以上网")
if age < 18:
    print("不可上网")
sent = 0
money = int(input('请告诉我你的资产:'))
if money >= 2:
    print("请上车")
    if sent >= 1:
        print("车上有空座请入座")
    if sent < 1:
        print('请您站着等待其他乘客下车')
else:
    print("没钱滚蛋")
