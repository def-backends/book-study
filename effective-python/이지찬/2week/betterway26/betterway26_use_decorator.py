from functools import wraps


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) '
              f'-> {result!r}')
        return result
    return wrapper


@trace
def fibonacci(n):
    """n 번째 피보나치 수를 반환한다."""
    if n in (0, 1):
        return n

    result = fibonacci(n - 2) + fibonacci(n - 1)
    return result


fibonacci = trace(fibonacci)
fibonacci(4)

"""
fibonaci를 호출 하면 trace의 인자로 greet 함수가 들어가게 되고
wrapper 함수가 fibonacci 함수를 호출하게 되고 fibonaccit의 인자값은 *args, **kwargs로 들어가게 된다.
fibonaci에 인자값은 *args로 들어가게 되고 **kwargs는 빈 딕셔너리로 들어가게 된다.
"""