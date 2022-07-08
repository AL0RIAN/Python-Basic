from typing import Callable
import functools

app = {}


def callback(route: str) -> Callable:
    def wrapper(func: Callable) -> Callable:
        app[route] = func

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            return result

        return wrapped

    return wrapper


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get("//")
if route:
    response = route()
    print('Ответ:', response)
else:
    print("Такого пути нет")
