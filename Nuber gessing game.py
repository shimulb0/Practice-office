students = []

while True:
    name = input('Enter student name: ')
    if name == 'end':
        print(students)
        print('Total students: ', len(students))
        break
    else:
        students.append(name)


import random
numbers = [1,2,3,4,5,6,7,8,9]
print('Guess a number between 1-9')
print('*' * 25)
computer_number = random.choice(numbers)
while True:
    number = int(input('Enter your number: '))
    print(number)
    if number == computer_number:
        print('Success, You have entered the right number', number)
        break
    else:
        print('Oh No', number, 'is not the right number')


