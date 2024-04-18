from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)


print("빨강", my_values.get('red'))
print("초록", my_values.get('green'))
print("파랑", my_values.get('blue'))
