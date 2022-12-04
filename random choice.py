import random
person = ['shimul','dhaka','barisal']
name = person[0]
living_place = person[1]
birth_place = person[2]
sentence1_group = [
    f'My name is {name.title()}.',
    f'Hello, I am {name.title()}.',
    f'This is {name.title()}.'
]
sentence2_group = [
    f'I live in {living_place.title()}.',
    f'I reside in {living_place.title()}.',
    f'I am in {living_place.title()} now.'
]
sentence3_group = [
    f'I was born in {birth_place}.',
    f'{birth_place.title()} is the place where I born.',
    f'My birth place is {birth_place}.'
]
sentence1 = random.choice(sentence1_group)
sentence2 = random.choice(sentence2_group)
sentence3 = random.choice(sentence3_group)
paragraph = sentence1 + ' ' + sentence2 + ' ' + sentence3
print(paragraph)