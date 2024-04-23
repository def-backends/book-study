def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)

    return result

visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)
assert sum(percentages) == 100.0

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

it = read_visits('/Users/bcd/Desktop/book-study/effective-python/이지찬/2week/betterway31/my_numbers.txt')
# percentages = normalize(it) # 여기서 제너레이터를 사용 했기 때문에 출력 []
# print(percentages)
print(list(it)) # 제너레이터를 사용하지 않고 리스트로 변환하여 출력 [15, 35, 80]
print(list(it)) # 이미 소진된 제너레이터를 사용하면 빈 리스트 출력 []


# 여행 데이터가 들어 있는 파일을 읽는 이터러블 컨데이너 클래스를 정의하는 코드
class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


def normalize(numbers):
    total = sum(numbers)
    breakpoint()
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


# 새로운 컨데이터 타입을 원래의 normalize 함수에 넘기면 코드를 전혀 바꾸지 않아도 함수가 잘 작동한다.
visits = ReadVisits("/Users/bcd/Desktop/book-study/effective-python/이지찬/2week/betterway31/my_numbers.txt")
percentages = normalize(visits)
print(percentages)
assert sum(percentages) == 100.0