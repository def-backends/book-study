fresh_fruit = {
    "사과": 10,
    "바나나": 8,
    "레몬": 5
}


def exam1():
    def make_lemonade(fruit_count):
        print(f"레몬 {fruit_count}개로 레몬에이드를 만듭니다")

    def out_of_stock():
        print("재고가 없습니다")

    count = fresh_fruit.get("레몬", 0)
    if count:
        make_lemonade(count)
    else:
        out_of_stock()

    if count := fresh_fruit.get("레몬", 0):
        make_lemonade(count)
    else:
        out_of_stock()


def exam2():
    count = fresh_fruit.get("바나나", 0)

    def slice_bananas(fruit_count):
        print(f"바나나 {fruit_count}개를 슬라이스합니다")
        return fruit_count

    def make_smoothies(fruit_pieces):
        print(f"{fruit_pieces}조각의 바나나 스무디를 만듭니다")
        return fruit_pieces

    if count >= 2:
        pieces = slice_bananas(count)
        to_enjoy = make_smoothies(pieces)

    else:
        count = fresh_fruit.get("사과", 0)
        if count >= 4:
            to_enjoy = make_smoothies(count)
        else:
            count - fresh_fruit.get("레몬", 0)
            if count:
                to_enjoy = make_smoothies(count)
            else:
                to_enjoy = "아무것도 없음"

    print(to_enjoy)


def exam3():
    def slice_bananas(fruit_count):
        print(f"바나나 {fruit_count}개를 슬라이스합니다")
        return fruit_count

    def make_smoothies(fruit_pieces):
        print(f"{fruit_pieces}조각의 스무디를 만듭니다")
        return fruit_pieces

    def make_juice(fruit_count):
        print(f"사과 {fruit_count}개로 주스를 만듭니다")
        return fruit_count

    def make_lemonaid(fruit_count):
        print(f"레몬 {fruit_count}개로 레몬에이드를 만듭니다")
        return fruit_count

    if (count := fresh_fruit.get("바나나", 0)) >= 9:
        pieces = slice_bananas(count)
        to_enjoy = make_smoothies(pieces)
    elif (count := fresh_fruit.get("사과", 0)) >= 4:
        to_enjoy = make_juice(count)
    elif (count := fresh_fruit.get("레몬", 0)) >= 1:
        to_enjoy = make_lemonaid(count)
    else:
        to_enjoy = "아무것도 없음"

    print(to_enjoy)
