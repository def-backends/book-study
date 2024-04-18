from itertools import zip_longest

names = ["이지찬", "BCD CORPORATION", "남궁민수"]
counts = [len(name) for name in names]

for i in range(len(names)):
    name = names[i]
    count = counts[i]
    print(f"{name}은 {count}글자")

for name, count in zip(names, counts):
    print(f"{name}은 {count}글자")

names.append("HOLLY WOOD")

for name, count in zip(names, counts):
    print(f"{name}은 {count}글자")

for name, count in zip_longest(names, counts):
    print(f"{name}은 {count}글자")
