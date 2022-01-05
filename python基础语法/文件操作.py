# f=open('test.txt','w')#写入后原有内容被覆盖，支持新建，支持写入
# f.write('aaa')#读写write，read
# f.close()
# f=open('test.txt','r')#报错，不支持写入，不支持新建文件
# f.write('bbb')
# f.close()
# f=open('1.txt','a')#a表追加，追加内容在文件末尾，支持写入，支持新建,原有内容不消失
# f.write('abc')
# f.close()
# f=open('test.txt')#打开方式可以省略，默认为r
# print(f.read(10))#\n算一个字节，所以你能看到的只有九个字符
# f.close()
f=open('test.txt')
# con1=f.readline()
# con2=f.readline()
# con3=f.readline()
# print(con1)
# print(con2)
# print(con3)
con4=f.readlines()
print(con4)
f.close()
