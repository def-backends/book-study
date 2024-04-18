from dataclasses import dataclass

numbers = [93, 86, 11, 68, 70]
numbers.sort()
print(numbers)


@dataclass(repr=True)
class Tool:
    name: str
    weight: float

result = Tool("수준계", 3.5)

print(result.__repr__())
eval("Tool(name='수준계', weight=3.5)")

class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"{self.name} ({self.weight}kg)"

    def __str__(self):
        return f"({self.weight}kg) {self.name} "


tools = [
    Tool("수준계", 3.5),
    Tool("해머", 1.25),
    Tool("스크류드라이버", 0.5),
    Tool("끌", 0.25),
]

# tools.sort()
tools.sort(key=lambda x: x.name)
print("이름순:", tools)

tools.sort(key=lambda x: x.weight)
print("무게순:", tools)

print("-"*100)
print(f"__repr__ : {repr(tools)}")
print(f"type __repr  : {type(repr(tools))}")
print(f"__str__ : {str(tools)}")
print(f"type __str__ : {type(str(tools))}")
print("-"*100)

print(f"__repr__ : {repr(tools[0])}")
print(f"type __repr  : {type(repr(tools[0]))}")
print(f"__str__ : {str(tools[0])}")
print(f"type __str__ : {type(str(tools[0]))}")
print("-"*100)
