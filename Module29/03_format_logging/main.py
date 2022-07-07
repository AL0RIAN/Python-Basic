import time
import functools
from typing import Callable, Optional


def logged(_func: Optional[Callable] = None, *, time_format: str, name_prefix="") -> Callable:
    """ Декоратор функции для логирования """

    def decorator(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs) -> Callable:
            start_time = time.time()
            print(f"- Запускается '{name_prefix + func.__name__}'. Дата и время запуска: {time.strftime(time_format)}")
            result = func(*args, **kwargs)
            end_time = time.time()

            print(f"- Завершение '{name_prefix + func.__name__}', время работы = {round(end_time - start_time, 3)}c")
            return result

        return wrapped

    if _func is None:
        return decorator
    return decorator(_func)


def log_method_call(time_format: str) -> Callable:
    """ Декоратор класса для декорирования всех его методов (кроме магических) """

    def decorator(cls):
        for i in dir(cls):
            if not i.startswith("__"):
                a = getattr(cls, i)
                decorated_a = logged(a, time_format=time_format, name_prefix=cls.__name__ + ".")
                setattr(cls, i, decorated_a)
        return cls

    return decorator


@log_method_call(time_format="%b %d %Y - %H:%M:%S")
class A:
    """ Тестовый класс с одним тестовым методом """

    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_method_call(time_format="%b %d %Y - %H:%M:%S")
class B(A):
    """ Наследник тестового класса A с двумя тестовыми методами """

    def test_sum_1(self) -> None:
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self) -> int:
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


if __name__ == "__main__":
    my_obj = B()
    my_obj.test_sum_1()
    my_obj.test_sum_2()
