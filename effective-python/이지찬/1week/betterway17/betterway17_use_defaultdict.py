visits = {
    'Mexico': {'Tulum', 'Puerto Vallarta'},
    'Japan': {'Hakone'},
}

visits.setdefault('France', set()).add('Khan')
if (japan := visits.get('Japan')) is None:
    visits['Japan'] = japan = set()

japan.add('Kyoto')

print(visits)


class Visits:
    def __init__(self):

        self.data = {}

    def add(self, country, city):
        city_set = self.data.setdefault(country, set())
        city_set.add(city)


visits = Visits()
visits.add('Russia', 'Moscow')
visits.add('Russia', 'Saint Petersburg')

print(visits.data)


from collections import defaultdict


class Visits:
    def __init__(self):
        self.data = defaultdict(set)
        self.data2 = defaultdict(list)
        self.data3 = defaultdict(int)

    def add_set(self, country, city):
        self.data[country].add(city)

    def add_list(self, country, city):
        self.data2[country].append(city)

    def add_count(self, country, count):
        self.data3[country] += count


visits = Visits()
visits.add_set('Russia', 'Moscow')
visits.add_set('Russia', 'Saint Petersburg')
visits.add_set('USA', 'Dallas')
visits.add_set('USA', 'Los Angeles')
visits.add_list('Russia', 'Moscow')
visits.add_list('Russia', 'Saint Petersburg')
visits.add_list('USA', 'Dallas')
visits.add_list('USA', 'Los Angeles')
visits.add_count('Russia', 1)
visits.add_count('Russia', 2)
visits.add_count('USA', 3)
visits.add_count('USA', 4)


print(visits.data)
print(visits.data2)
print(visits.data3)


def greet(**kwargs):
    if (name := kwargs.get("name")) and (age := kwargs.get("age")):
        print(f"Hello, {name}! You are {age} years old.")
    else:
        print("Hello, stranger!")


greet(name='Alice', age=25)
greet(name='Bob')

from collections import defaultdict

class GradeTracker:
    def __init__(self):
        self.grades = defaultdict(list)

    def add_grade(self, student, subject, grade):
        self.grades[student].append((subject, grade))

    def get_grades(self, student):
        return self.grades.get(student)


tracker = GradeTracker()
tracker.add_grade('Alice', 'Math', 90)
tracker.add_grade('Alice', 'Science', 85)
tracker.add_grade('Bob', 'Math', 88)

print(tracker.get_grades('Alice'))
print(tracker.get_grades('Bob'))
