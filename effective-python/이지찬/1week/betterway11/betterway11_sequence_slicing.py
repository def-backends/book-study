a = ["A", "B" , "C", "D", "E", "F", "G", "H"]
print(f"가운데 2개: {a[3:5]}")
print(f"마지막을 제외한 나머지: {a[1:7]}")

assert a[:5] == a[0:5]
assert a[5:] == a[5:len(a)]

print(a[:])  # 전체
print(a[:20])  # 인덱스 길이가 넘어가도 에러 발생하지 않음
print(a[20:])  # 인덱스 길이가 넘어가도 에러 발생하지 않음
print(a[-1:])  # 마지막 요소만
print(a[:-1])  # 마지막 요소 제외
print(a[:-0])
print(a[-0:])

b = a[3:]
print(b)
b[1] = 99
print(b)
print(a)
_a = a
print(_a)

del(_a[1])

b = a
assert a == b
a[:] = ["가", "나", "다"]
assert a == b
c = ["가", "나", "다"]
assert a == c
assert b == c

c[2:7] = [99, 22, 14]
