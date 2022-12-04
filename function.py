# def number(x,y):
#     sum = x + y
#     return sum
# print(number(20,60))
#
# def number(x):
#     math = x**3 + x*9 - 8
#     return math
# print(number(2))


def urlify(text):
    slag = text.strip().lower().replace(' ','-')
    while '--' in slag:
        slag = slag.replace('--','-')
    return slag

title = input('Enter Title: ')
slag = urlify(title)
print(slag)
