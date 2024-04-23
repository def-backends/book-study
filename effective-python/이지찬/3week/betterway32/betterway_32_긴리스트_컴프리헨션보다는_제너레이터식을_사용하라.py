value = [len(x) for x in open('/effective-python/이지찬/2week/betterway32/my_file.txt')]
# len(value): 16568031

it = (len(x) for x in open('/effective-python/이지찬/2week/betterway32/my_file.txt'))
print(next(it))
print(next(it))
