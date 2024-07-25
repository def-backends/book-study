"""
주요 키워드: 공개속성, private 속성, 접근성?

불필요한 private 속성사용을 피하고 공개 속성을 사용
"""

class MyClass:
    def __init__(self):
        self.public_attribute = "public"
        self._private_attribute = "private"


obj = MyClass()
print(obj.public_attribute)
print(obj._private_attribute) # 되긴 하는데 가급적 쓰지 말기
