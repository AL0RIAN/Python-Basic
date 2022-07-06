from typing import Callable
import functools


def decorator_with_args_for_any_decorator(decorated_to_enhance: Callable) -> Callable:
    """ Декоратор дает возможность другому декоратору принимать произвольные аргументы """

    def decorator_maker(*args, **kwargs) -> Callable:
        def decorator_wrapper(func: Callable) -> Callable:
            return decorated_to_enhance(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *dec_args, **dec_kwargs) -> Callable:
    """ Шаблонный декоратор """

    @functools.wraps(func)
    def wrapper(*func_args, **func_kwargs) -> Callable:
        print("Название:", func.__name__)
        print("Переданные args и kwargs в декоратор:", dec_args, dec_kwargs)
        return func(*func_args, **func_kwargs)

    return wrapper


@decorated_decorator(10011, [1, 2, 3, 4, 5], "Hi", {1: "a", 2: "b", 3: "c"})
def test(name: str, greet: str) -> None:
    print(f"{greet}, {name}")


if __name__ == "__main__":
    test("Kirill", "Hello")
