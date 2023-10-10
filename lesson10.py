# Декораторы

# def my_decorator(func):
#     def wrapper():
#         print("То что выходит до функции")
#         print(func())
#         b = func()
#         print(b + 10)
#     return wrapper


# @my_decorator
# def hello():
#     n = 5 + 5
#     return n

# hello()


# def repeat(num):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(num):
#                 func(*args,**kwargs)
#         return wrapper
#     return decorator
    
# @repeat(3)
# def say_hello():
#     print('hello')

# say_hello()
            
def auth_decor(func):
    def wrapper(username,passwors,*args,**kwargs):
        if username == 'admin' and passwors == 'secret':
            result = func(*args, **kwargs)
        else:
            result = 'Error'
        return result
    return wrapper

@auth_decor
def my_func():
    return 'Dostup razreshen'

print(my_func('admin','secret'))











