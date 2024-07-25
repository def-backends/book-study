"""
주요 키워드: 다중상속, 다이아몬드 상속, MRO, super()
MRO(Method Resolution Order): 파이썬이 메서드나 속성을 검색하는 순서

다중상속, 다이아몬드 상속시 부모클래스의 초기화는 super()을 통해 초기화를 해야 하며 부모클래스.__init__으로 초기화를 하게되면
중복 초기화가 발생하므로 super()를 통한 초기화를 하여 중복 초기화를 방지 한다.

IDE에서 잡아주긴 한다.
"""
class Parent:
    def __init__(self, value):
        self.value = value


class Child1(Parent):
    def __init__(self, value):
        super().__init__(value)
        self.value *= 5



class Child2(Parent):
    def __init__(self, value):
        super().__init__(value)
        self.value += 10


class OneWay(Child1, Child2):
    def __init__(self, value):
        super().__init__(value)

last = OneWay(5)