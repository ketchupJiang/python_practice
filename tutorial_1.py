# variable
name = 'yojer liu'
print(name.title()) # 各单词首字母大写
print(name.upper()) # 所有字母均大写
name = 'Yojer Liu'
print(name.lower()) # 所有字母均小写
print('================================')

anotherName = 'Yojer     '
print(len(anotherName))
# 消除字符串尾部多于的空格
print(anotherName)
print(anotherName.rstrip())
print(len(anotherName.rstrip()))
print('================================')

anotherName = '     Yojer'
print(len(anotherName))
# 消除字符串首部多余的空格
print(anotherName.lstrip())
print(len(anotherName.lstrip()))
print('================================')

# 消除字符串前后多余的空格
anotherName = '     Yojer     '
print(len(anotherName))
print(len(anotherName.strip()))

# 字符串拼接
message1 = 'Yojer'
message2 = 'Liu'
message3 = message1 + message2
print(message1 + message2)
print(message3)
age = 100 # int: integer
print(age * 2)
print(age**2) #age^2
print(age**3) #age^3
print(age + 300)
print(age / 33)
print('============================')

# \n 换行符
print("What's up?\nNothing.")
# \t 制表符
print("\tWhat's up?")
print()
print("What's up?")
print('Nothing.')

# 字符串拼接
print(message1 + str(age) + message2)


