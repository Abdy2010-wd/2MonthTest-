from datetime import datetime as dt


def checktime(func):
    def wrapper(*args, **kwargs):
        time_now = dt.now()
        print(
            f"функция была вызвана в "
            f"{time_now.hour:02}:{time_now.minute:02}:{time_now.second:02} "
            f"{time_now.day:02}/{time_now.month:02}/{time_now.year}"
        )
        return func(*args, **kwargs)
    return wrapper


@checktime
def hello_world():
    print("hello world")


if __name__ == "__main__":
    hello_world()