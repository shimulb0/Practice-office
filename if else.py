min_age_to_vote = 18
age = int(input('Enter your age: '))
if age >= min_age_to_vote:
    if age >= 50:
        print(f'Kaka you are {age}. Onek vote disen, ar dorkar nai ')
    else:
        print(f'You are {age}. And you can vote now')
else:
    print(f'Hello babu, You are {age} And you can vote after', min_age_to_vote - age, 'years')