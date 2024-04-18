items = ["apple", "banana", "apple", "orange", "banana", "apple"]

# 조건문을 사용하여 키의 존재 여부 확인
counter = {}
for item in items:
    if item in counter:
        counter[item] += 1
    else:
        counter[item] = 1

print(f"not nice: {counter}")

# get() 메서드를 사용하여 키의 존재 여부 확인 및 기본값 설정
counter = {}
for item in items:
    counter[item] = counter.get(item, 0) + 1

print(f"nice: {counter}")
