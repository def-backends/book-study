stock = {
    "못": 125,
    "나사못": 35,
    "나비너트": 8,
    "와셔": 24
}

order = ["나사못", "나비너트", "클립"]


def get_batches(count, size):
    return count // size


result = {}
for name in order:
    count = stock.get(name, 0)
    batches = get_batches(count, 8)
    if batches:
        result[name] = batches

print(result)

found = {
    name: get_batches(stock.get(name, 0), 8)
    for name in order
    if get_batches(stock.get(name, 0), 8)
}

print(found)

found2 = {
    name: batches for name in order
    if (batches := get_batches(stock.get(name,0), 8))
}
print(found2)
