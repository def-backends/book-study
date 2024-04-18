def remainder(number, divisor):
    return number % divisor


assert remainder(20, 7) == 6
remainder(20, 7)
remainder(20, divisor=7)
remainder(number=20, divisor=7)
remainder(divisor=7, number=20)

def print_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_parameters(alpha=1.5, beta=9, gamma=4)