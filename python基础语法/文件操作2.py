# 文件对象.seek(偏移量，起始位置)0开头1当前2结尾
# f = open('test.txt', 'r+')#默认文件指针在开头
# f.seek(2, 0)
# con = f.read()
# print(con)
# f.close()
# f = open('test.txt', 'a+')#默认文件指针在结尾
# f.seek(0, 0)#两个0可以写成一个
# con = f.read()
# print(con)
# f.close()
import os

# os.rename('1.txt','10.txt')
# os.remove('10.txt')
# os.mkdir('aa')#创建文件夹
# os.rmdir()#删除文件夹
# os.chdir('aa')#切换文件路径
# os.mkdir('bb')#在‘aa’中创建bb
print(os.listdir())  # 查看文件夹目录返回列表
print(os.getcwd())  # 返回当前文件所在路径
