str1 = 'hello'
str2 = 'hello12345'
str3 = '12345'
str4 = '     '
str5 = "hello world and apple and orange and banana"
print(str1.isalpha())#isalpha全是字母返回ture
print(str5.isalpha())#有空格也返回false
print(str3.isdigit())#isdigit全是数字返回ture
print(str2.isalnum())#isalnum全是字母或数字组合返回ture
print(str4.isspace())#全是空格返回ture
#打is有代码提示