# Файлы чтения и запись

# file = open('text.txt','r')#encoding='utf-8'

# content = file.read()
# print(content)

# file.close()

# with open('text.txt','w',encoding='utf-8') as file:
#     content = file.read()
#     print(content) это чистка файла и новая запись

# with open('text.txt','r',encoding='utf-8') as file:
#     content = file.read()
#     print(content) это чтение файла

# with open('text.txt','a',encoding='utf-8') as file:
#     content = file.read()
#     print(content) это запись файла без очистки его внутри


# with open('text.txt','w',encoding='utf-8') as file:
#     lines = ['Строка 1','Строка 2']
#     content = file.writelines(lines)
#     print(content) 

# with open('text.txt','w',encoding='utf-8') as file:
#     n = 10*10
#     content = file.write(str(n))
#     print(content)

# with open('text.txt','w',encoding='utf-8') as file:
#     user = str(input())
#     content = file.write(user)
#     print(content)

# with open('text.txt','a',encoding='utf-8') as file:
#      user = str(input())
#      content = file.write(user)
#      print(content)

# with open('text.txt','r',encoding='utf-8') as file:
#     for l in file:
#         print(l)


# with open('text.txt','r',encoding='utf-8') as file:
#     with open('copy.txt','w',encoding='utf-8') as copy_file:
#         copy_file.write(file.read())



# with open('text.txt','a',encoding='utf-8') as file:
    #  user = str(input())
    #  content = file.write(user)
    #  print(content)


# with open('text.txt','r',encoding='utf-8') as file:
#     content = file.read()

# new_content = content.replace('собачка','Собачка')


# with open('text.txt','w',encoding='utf-8') as new_file:
#     new_file.write(new_content)


























