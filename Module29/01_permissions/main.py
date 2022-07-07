import functools
from typing import Callable, Optional

user_permissions = ['admin', 'user']


def check_permissions(_func: Optional[Callable] = None, *, permission: str) -> Callable:
    def check(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            try:
                if permission in user_permissions:
                    result = func(*args, **kwargs)
                    return result
                else:
                    raise PermissionError(f"У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}")
            except PermissionError as error:
                print(f"{error.__class__.__name__}: {error}")

        return wrapped

    if _func is None:
        return check
    return check(_func)


@check_permissions(permission="admin")
def delete_site():
    print('Удаляем сайт')


@check_permissions(permission="user")
def add_comment():
    print('Добавляем комментарий')


@check_permissions(permission="visitor")
def to_favorite():
    print('Добавляем в избранное')


if __name__ == "__main__":
    delete_site()
    add_comment()
    to_favorite()
