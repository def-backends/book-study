lengths = [10, 20, 30, 40, 50, 60]


def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum


minimum, maximum = get_stats(lengths)
print(f'Min: {minimum}, Max: {maximum}')


def get_avg_ratio(numbers):
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse=True)
    return scaled


longest, *middle, shortest = get_avg_ratio(lengths)
print(f'Longest: {longest}, Shortest: {shortest}, Middle: {middle}')

