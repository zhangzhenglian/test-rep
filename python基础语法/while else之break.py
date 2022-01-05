i = 0
while i < 5:
    if i == 3:
        #print('行了，一点也不真诚')
        print("能不能真诚一点")
        #break
        i += 1
        continue

    print('老婆，我错了')
    i = i+1
else:                      #break终止循环else不执行
    print('老婆原谅我了')