def my_decorator(func):
    print("test")# func 是通用参数，可以接受任何函数
    def wrapper():
        print("函数执行前")
        func(2) # 这里动态调用被修饰的函数
        print("函数执行后")
    return wrapper
# 使用修饰符
@my_decorator
def say_hello(name):
    print("Hello!")
    print(name)

# 实际等价于：
# say_hello = my_decorator(say_hello)
if __name__ == "__main__":
    say_hello()