import math

def wave(amplitude, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        yield output


def transmit(output):
    if output is None:
        print(f'Output is None')
    else:
        print(f'Output: {output:>5.1f}')


def run(it):
    for output in it:
        transmit(output)


run(wave(3.0, 8))


def my_generator():
    received = yield 1
    print(f'received = {received}')

it = my_generator()
output = next(it)
print(f'output = {output}')

try:
    next(it)
except StopIteration:
    pass

def my_generator():
    received = yield 1
    print(f'received = {received}')

it = iter(my_generator())
output = it.send(None)  # Unresolved attribute reference 'send' for class 'Iterator'
print(f'output = {output}')

try:
    it.send('hello')
except StopIteration:
    print("StopIteration")


def wave_cascading(amplitude_it, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        amplitude = next(amplitude_it)
        output = amplitude * fraction
        yield output


def complex_wave_cascading(amplitude_it):
    yield from wave_cascading(amplitude_it, 3)
    yield from wave_cascading(amplitude_it, 7)
    yield from wave_cascading(amplitude_it, 15)


def run_cascading():
    amplitudes = [2.0, 3.0, 1.0, 1.5, 2.5]
    it = complex_wave_cascading(iter(amplitudes))
    for wave_output in it:
        transmit(wave_output)


run_cascading()
