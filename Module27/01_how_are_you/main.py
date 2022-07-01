import functools
from typing import Callable, Any


def terror(func: Callable) -> Callable:
    """Output Как дела? and а У мЕнЯ нЕ оЧеНь! before wrapped function"""
    @functools.wraps(func)
    def wrapped(*args, **kwargs) -> Any:
        input('Как дела? ')
        print('а У мЕнЯ нЕ оЧеНь!')
        result = func(*args, **kwargs)

    return wrapped


@terror
def test():
    """Output '<Тут что-то происходит...>'"""
    print('<Тут что-то происходит...>')


if __name__ == "__main__":
    test()
