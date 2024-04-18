from abc import ABC, abstractmethod
"""
특정 객체의 최상위 공통 카테고리의 추상 클래스를 만들고, 이 클래스를 상속받아서 구체적인 객체를 생성
예를 들어 
사람이라면 인종으로 구분 지을수 있고 인종은 다시 흑인, 백인, 황인으로 구분지을수 있다.
혹은 속한 나라로 구분 지을수 있고 나라는 다시 한국, 미국, 일본으로 구분지을수 있다.
"""


class Car(ABC):
    @abstractmethod
    def create(self):
        pass


class Taxi(Car):
    def create(self):
        return "Taxi"


class Bus(Car):
    def create(self):
        return "Bus"


class Truck(Car):
    def create(self):
        return "Truck"


CLASSES = {"taxi": Taxi,
           "bus": Bus,
           "truck": Truck}


class CarFactory:
    @classmethod
    def create_car(cls, car_type, classes=None):
        if classes is None:
            classes = CLASSES

        if car_type not in classes:
            raise ValueError("올바른 자동차 타입이 아닙니다.")

        return classes[car_type]().create()


taxi = CarFactory.create_car("taxi")
bus = CarFactory.create_car("bus")
truck = CarFactory.create_car("truck")

print(f"create {taxi}")
print(f"create {bus}")
print(f"create {truck}")

# sports_car = CarFactory.create_car("sports car")  # ValueError: 올바른 자동차 타입이 아닙니다.


class Human(ABC):
    @abstractmethod
    def human_from(self):
        pass


class Korean(Human):
    def human_from(self):
        return "Korean"


class Japanese(Human):
    def human_from(self):
        return "Japanese"


class American(Human):
    def human_from(self):
        return "American"


class HumanFrom:
    @classmethod
    def born(cls, from_country):
        if from_country == "korea":
            return Korean().human_from()
        if from_country == "japan":
            return Japanese().human_from()
        if from_country == "america":
            return American().human_from()

        raise ValueError("존재하지 않는 국가 입니다.")


korean = HumanFrom.born("korea")
japanese = HumanFrom.born("japan")
american = HumanFrom.born("america")

print(f"where are you from? i'm {korean}")
print(f"where are you from? i'm {japanese}")
print(f"where are you from? i'm {american}")
