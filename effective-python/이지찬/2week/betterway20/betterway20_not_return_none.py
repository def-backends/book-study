def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e

x, y = 5, 2
result = careful_divide(x, y)
if result is None:
    print('Invalid inputs')
