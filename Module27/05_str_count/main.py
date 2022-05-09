import functools
from typing import Callable, Any


def counter(func: Callable) -> Callable:
    """Counts number of the function calls """
    @functools.wraps(func)
    def wrapped(cache={}, *args, **kwargs) -> Any:
        if func.__name__ in cache.keys():
            cache[func.__name__] += 1
        else:
            cache[func.__name__] = 1
        result = func(*args, **kwargs)
        print(f'Функция {func.__name__} была вызвана {cache[func.__name__]} раз(а)\n')
        return result

    return wrapped


@counter
def test_1():
    """Output '<Тут что-то происходит...>'"""
    print('<Тут что-то происходит...>')


@counter
def test_2():
    """Output '<Тут ничего не происходит...>'"""
    print('<Тут ничего не происходит...>')


if __name__ == "__main__":
    test_1()
    test_1()
    test_1()
    test_2()
    test_2()
    test_2()
