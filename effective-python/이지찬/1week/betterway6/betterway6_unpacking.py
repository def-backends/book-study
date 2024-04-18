snacks = [("bacon", 350), ("donut", 240), ("muffin", 190)]
snacks2 = [{"bacon", 350}, {"donut", 240}, {"muffin", 190}]


def print_snack1():
    for i in range(len(snacks)):
        item = snacks[i]
        name = item[0]
        calories = item[1]
        print(f"#{i + 1}: {name}은 {calories} 칼로리")

    for rank, (name, calories) in enumerate(snacks, 1):
        print(f"#{rank}: {name}은 {calories} 칼로리")


def print_snack2():
    for rank, (name, calories) in enumerate(snacks2, 1):
        print(f"#{rank}: {name}은 {calories} 칼로리")


print_snack1()
print_snack2()