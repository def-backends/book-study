def sort_priority2(numbers, group):
    found = False

    def helper(x):
        if x in group:
            nonlocal found
            found = True
            return 0, x
        return 1, x

    numbers.sort(key=helper)
    return found


print(sort_priority2([1,2,3], [4,5,6]))


class Sorter:
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return 0, x
        return 1, x


group = [3, 4, 5]
numbers = [1, 2, 3, 4, 5, 6]

sorter = Sorter(group)
numbers.sort(key=sorter)
print(f"sorter.found: {sorter.found}")
assert sorter.found is True
