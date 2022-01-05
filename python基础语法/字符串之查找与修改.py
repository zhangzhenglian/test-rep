str1 = "hello world and apple and orange and banana"
print(str1.find('and',15,30))#没有报-1
print(str1.rfind('and'))#从右侧开始查找
print(str1.index('and',15,30))#没有报错
print(str1.rindex('and'))#从右侧开始查找
print(str1.count('and'))#出现次数，没有报0
new_str = str1.replace('and','or',2)#(旧，新，替换次数）
print(new_str)
print(str1.split('and'))
print(str1.split(' '))#中间有一个空格，意思是在空格处分割
print(str1.split('and',2))#2代表分割次数
list=['aa','bb','cc']
print('_'.join(str1))
print('_'.join(list))
#'子'.join(多字符序列)
