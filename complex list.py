person = [
    ['Moris','male','australia','1988','moris@jon.com'],
    ['Vasko','male','Ukrain','1956','vaso@jon.com'],
    ['Amni','female','Norway','1926','amni@jamni.com'],
    ['Jane','female','Bangladesh','1966','james@jamni.com'],
    ['Andrew','male','India','1985','andy@sandy.com'],
]
i = 0
while i < len(person):
    single_person = person[i]
    name = single_person[0]
    gender = single_person[1]
    country = single_person[2]
    birth_year = single_person[3]
    email = single_person[4]
    if gender == 'male':
        pronoun = 'he'
        rel_pronoun = 'his'
    else:
        pronoun = 'she'
        rel_pronoun = 'her'
    paragraph = f'{name.title()} lives in {country.title()}. {pronoun.title()} was born in {birth_year}. {rel_pronoun.title()} email is {email}'
    print(paragraph)
    i += 1

