
baby_names = {
    "cat": "kitten",
    "dog": "puppy"
}
print(baby_names)

print(list(baby_names.keys()))
print(list(baby_names.values()))
print(list(baby_names.items()))
print(baby_names.popitem())


def my_func(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


my_func(goose="gosling", kangaroo="joey")


votes = {
    "otter": 1281,
    "polar bear": 587,
    "fox": 863
}


def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i


def get_winner(ranks):
    return next(iter(ranks))


ranks = {}
populate_ranks(votes, ranks)
print(ranks)
winner = get_winner(ranks)
print(winner)


from collections import OrderedDict

# OrderedDict를 생성합니다.
ordered_dict = OrderedDict()

# 여러 항목을 순서대로 삽입합니다.
ordered_dict['apple'] = 1
ordered_dict['banana'] = 2
ordered_dict['cherry'] = 3

# 삽입된 순서대로 출력합니다.
for key, value in ordered_dict.items():
    print(key, value)


ordered_dict = {"A": 1}
ordered_dict.update({"B": 2})
ordered_dict.update({"C": 3})

for key, value in ordered_dict.items():
    print(key, value)
