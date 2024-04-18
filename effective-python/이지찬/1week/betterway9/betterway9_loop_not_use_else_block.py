def exam1():
    for i in range(3):
        print(i)
    else:
        print("else block")


def exam2():
    for i in range(3):
        print(i)
        if i == 1:
            break
    else:
        print("else block")


def exam3(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True


assert exam3(4, 9)
assert not exam3(3, 6)


def exam4(a, b):
    is_comprime = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_comprime = False
            break

    return is_comprime


assert exam4(4, 9)
assert not exam4(3, 6)
