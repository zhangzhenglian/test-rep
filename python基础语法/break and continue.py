i = 1
while i <= 5:
    if i == 4:
      print('烂苹果，不吃，吃下一个')   # print("吃饱了，不吃了")
      i+=1   #continue:跳过当前循环直接进入下一个循环（没有这一步陷入死循环）
      continue                               #break
    print(f'吃了第{i}个苹果')
    i = i + 1