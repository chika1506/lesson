# Исключения

# try:
#     num = int(input('Vvedite chislo: '))
#     res = 10 / num
#     print(res)
# except Exception as re:
#     print('Error')

# except ValueError as ve:
#     print('Ошибка значений {0}' .format(ve))
# except ZeroDivisionError:
#     print('Ошибка делений')
# finally :
#     print(" Ура заработал ")
# print('ok')

# try:
#     num2 = int(input('Vvedite chislo: '))
#     res2 = 2 / num2
#     print(res2)
# except (ValueError,ZeroDivisionError)                                                                                  :
#     print('Ошибка')


# num = int(input('Введите число: '))

# 1)
#  if num % 2 == 0:
#     print('Четное число')
# else:
#     print('Нечетное число')  

# 2) 

# num1 = float(input("Введите первое число: "))
# m = input("Введите оператор (+, -, *, /): ")
# num2 = float(input("Введите второе число: "))

# if m == "+":
#     print("Результат: ", num1 + num2)
# elif m == "-":
#     print("Результат: ", num1 - num2)
# elif m == "*":
#     print("Результат: ", num1 * num2)
# elif m == "/":
#     if num2 != 0:
#         print("Результат: ", num1 / num2)
#     else:
#         print("Ошибка!")
# else:
#     print("Ошибка!")

# m = 'Привет мир'
# n = m.split() 
# print(' '.join(n[::-1]))

# def cesar(text,shift):
#     result = ''
#     alphabet_lower = 'abcdefghijkolmnpqrstuw'
#     # alphabet_upper = 'ABCDEFGHIJKOLMNPQRSTUW'
#     for i in text:
#         is_upper = str(i).upper()
#         if str(i).isalpha():
#             i_index = alphabet_lower.index(i)
#             i_shift = alphabet_lower[(i_index + shift)] % 26
#             result +=i_shift if not is_upper else i_shift.upper()
#         else:
#             result += i

# inp_text = 'abc xyz'
# shift_v = 3
# enc_text = cesar(inp_text,shift=shift_v)
# print(enc_text)


















































