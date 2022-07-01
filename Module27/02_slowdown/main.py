import time
import functools
from typing import Callable, Any


def slowpoke(func: Callable) -> Callable:
    """Decorator. It slows down the function"""
    @functools.wraps(func)
    def wrapped(*args, **kwargs) -> Any:
        start = time.time()
        time.sleep(5)
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Функция выполнялась {end - start} с")
        return result

    return wrapped


@slowpoke
def test():
    """Output '<Тут что-то происходит...>'"""
    print('<Тут что-то происходит...>')


if __name__ == "__main__":
    test()
