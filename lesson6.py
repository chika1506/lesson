# Функции в python

# def name_function():
#     telo functii
#     deistvie functii 

# name = 'Jhon' Глобальный

# def n():
#     name = 'Cage' Локальный
#     print('hello world',name)
# n()
# print(name)


# def n(name):
#     print('hello world',name)
# n('Jnon')


# n1 = 'Jhon'
# def n(name):
#     print('hello world',name)
# n(name=n1) Аргументы можно приравнивать с переменными глобальной части



# def sqad(number):
#     return number * number  #возвращает

# result = sqad(7)
# print(result)



# def sqad(num,m):
#     a = num * num
#     b = a * m
#     n = b + 5
#     return print(b,n)

# n = int(input())
# m = int(input())
# sqad(num=n,m=m)

# def hi(name='neznakomec'):
#     return print(f'привет {name}')

# name = str(input())

# hi()
# hi('anna')
# hi('jhon')
# hi('lol')
# hi(name=name)


# def fact(n):
#     if n == 0:
#         return 1
#     else :
#         return n * fact(n-1)

# ressult = fact(3)
# print(ressult)

# lambda аргументы : выражения Анонимная функция без имени

# num = lambda x,y : x + y
# result = num(5,4)
# print(result)

# word = ['applee',"gr","orangee"]
# word.sort(key=lambda word: len(word))
# print(word)

# def name(*args,**kwargs):
#     print(args,kwargs)

# # *args позиционный аргумент
# # **kwargs именованный аргумент
# name('Jhon')


