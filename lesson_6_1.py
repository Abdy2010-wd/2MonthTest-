def printer(func):
    def wrapper(*args, **kwargs):
        print(f"До вызова ф-ии {func.__name__}")
        result = func(*args, **kwargs)
        print(f"После вызова ф-ии {func.__name__}")
        return result

    return wrapper

@printer
def hello_world():
    print("hello world")

def add_numbers(number1, number2):
   return number1 + number2






 