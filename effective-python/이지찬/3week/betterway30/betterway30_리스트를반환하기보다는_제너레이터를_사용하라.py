import itertools


def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result

address = "컴퓨터(영어: Computer, 문화어: 콤퓨터, 순화어: 전산기)는 집합적으로 프로그램 가능한 계산기를 가리키는 말이다."
result = index_words(address)
print(result)


def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


iter_result = index_words_iter(address)
result = list(iter_result)
print(result)


def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset


with open('/Users/bcd/Desktop/book-study/effective-python/이지찬/2week/betterway30/address.txt', 'r') as f:
    it = index_file(f)
    results = itertools.islice(it, 0, 10)
    print(list(results))

