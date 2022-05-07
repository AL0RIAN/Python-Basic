import datetime
import functools
from typing import Callable, Any


def logging(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped(*args, **kwargs) -> Any:
        try:
            print(f'Function name: {func.__name__}\n'
                  f'Documentation: {func.__doc__}\n\n'
                  )
            result = func(*args, **kwargs)
            return result
        except Exception as error:
            with open('function_errors.log', 'a') as file:
                file.write(
                    f'Time: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}\n'
                    f'Function name: {func.__name__}\n'
                    f'Error name: {error.__class__.__name__}\n\n'
                )

    return wrapped


@logging
def test(num: int) -> (bool, KeyError):
    """If num = 1 it returns True"""
    if num == 1:
        return True
    elif num == 2:
        raise EOFError
    elif num == 3:
        raise IndexError
    else:
        raise KeyError


if __name__ == "__main__":
    test(0)
    test(1)
    test(1)
    test(2)
    test(3)
