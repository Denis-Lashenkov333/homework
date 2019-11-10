import random
english=list("+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
russian = list("+-/*!&$#?=@<>1234567890ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁйцукенгшщзхъфывапролджэячсмитьбюё")
x=str(input("использовать кириллицу?")) 
number = int(input("количество паролей:"))
length = int(input("длина пароля:"))
if x.upper()=="ДА":
    for n in range(number):
        password = ''
        for i in range(length):
            password += random.choice(russian)
        print(password)    
else:
    for n in range(number):
        password = ''
        for i in range(length):
            password += random.choice(english)
        print(password)
my_file=open("my_file.txt","w")
my_file.write(password)
my_file.close()
