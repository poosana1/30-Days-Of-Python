# 1
thirty = 'Thirty '
days = 'days '
of =  'of '
python = 'python'
print(thirty + days + of + python)

# 2
coding = 'coding '
ffor = 'for '
all = 'all'

# 3, 4
company = coding + ffor + all
print(company) 

# 5 
print(len(company))

# 6
print(company.upper())

# 7
print(company.lower())

# 8
print(company.capitalize(), company.title(), company.swapcase())

# 9
print(company[7:])

# 10
print(company.find('Coding'))

# 11
print(company.replace('coding', 'Python'))

# 12, 13
print(company.split(' '))

# 14
sp = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(sp.split(','))

# 15
print(company[0])

# 16
print(company.rindex('l'))

# 17
print(company[10])

# 18
all_people = 'Coding For All People.'
print(all_people.rfind('l'))

# 23
print('You cannot end a sentence with because because because is a conjunction'.find('because'))

# 24
print('You cannot end a sentence with because because because is a conjunction'.rfind('because'))

# 25
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:55])

# 26, 27 
print(sentence.index('because'))

# 28
print('Coding for all'.startswith('Coding'))

# 29 
print('Coding for all'.endswith('Coding'))

# 30
print('   Coding for all  '.strip())

# 32
libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(libs))

# 33
print('I am enjoying this challenge.\nI just wonder what is next.')

# 34
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFindland\tHelsinki')

# 35
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square.')

# 36
a = 8;b = 6
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')


