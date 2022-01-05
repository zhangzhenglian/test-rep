def info_print():
    print('请选择功能')
    print('1.添加学员')
    print('2.删除学员')
    print('3.修改学员')
    print('4.查询学员')
    print('5.显示所有学员')
    print('6.退出系统')
    print('-' * 20)


# break用来终止本次循环，return直接跳出整个函数

info = []


def info_stu():
    '''添加学员函数'''
    new_id = input("请输入新学员学号:")
    new_name = input("请输入新学员姓名:")
    new_tel = input("请输入新学员手机号:")
    global info  # 没有这一步，则不会储存字典进列表(退出程序后不储存)
    for i in info:
        if new_name == i['name']:
            print('此姓名已存在')
            return
    dict1 = {}
    dict1['id'] = new_id
    dict1['name'] = new_name
    dict1['tel'] = new_tel
    info.append(dict1)
    print(info)

    pass


def del_info():
    del_name = input('请输入您要删除的姓名：')
    global info
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            print('删除成功')
            break  # 只能跳循环,且只能跳一层循环,对if else语句不起作用
    else:  # 和谁并列对谁负责,如果for else正常执行完毕会执行else,如果通过break退出则不执行
        print('您输入的姓名不存在')


while True:
    info_print()
    user_num = int(input("请输入功能序号:"))
    if user_num == 1:
        info_stu()
        # print('添加')
    elif user_num == 2:
        del_info()
        # print('删除')
    elif user_num == 3:
        print('修改')
    elif user_num == 4:
        print('查询')
    elif user_num == 5:
        print('显示所有')
    elif user_num == 6:
        print('退出系统')
    else:#多个if并列else只与最近的if匹配,所有要用elif
        print('您输入的序号有误，请重新输入')
