import functools
from typing import Callable, Any


def debug(func: Callable) -> Callable:
    """Debug decorator"""
    @functools.wraps(func)
    def wrapped(*args, **kwargs) -> Any:
        print(f'{func.__name__}({", ".join([repr(i) for i in args] + [f"{x}={repr(y)}" for x, y in kwargs.items()])})')
        result = func(*args, **kwargs)
        print(f'{repr(func.__name__)} вернула значение {repr(result)}\n')
        return result

    return wrapped


@debug
def greeting(name: str, age=None) -> str:
    """Returns a greeting with given name and age (if age was given)"""
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


if __name__ == "__main__":
    greeting("Том")
    greeting("Миша", age=100)
    greeting(name="Катя", age=16)
