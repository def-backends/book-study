car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)
# oldest, second_oldes = car_ages_descending  # value error

oldest = car_ages_descending[0]
second_oldes = car_ages_descending[1]
others = car_ages_descending[2:]
print(oldest, second_oldes, others)

oldest, second_oldest, *others = car_ages_descending
print(oldest, second_oldest, others)

car_inventory = {
    "시내": ("그랜저", "아반떼", "소나타", "티코"),
    "공항": ("제네시스 쿠페", "소나타", "아반떼", "그랜저"),
}

((loc1, (best1, *rest1)), (loc2, (best2, *rest2))) = car_inventory.items()
print(f"{loc1} 최고: {best1}, 나머지: {rest1}")
print(f"{loc2} 최고: {best2}, 나머지: {rest2}")
