name = 'Матвеева Арина'
age = 19
print('я ', name, 'и мне ', age, 'но уже скоро будет', age + 1)

name1 = 'Арина'
n = 5
for i in range(n):
    print(name1)

name2 = input('можно ваше имя?')
age2 = input('а сколько вам лет?')
print('приветствую вас, ', name2, 'я знаю ваш возраст! вам', age2, 'я прав??')

age3 = int(input('ваш возраст??'))
if age3 < 18:
    print('хмм, ты ещё мал чтобы покупать алкоголь')
else:
    print('вау, а ты уже большой, поздравляю!!!')

name3 = input('имя?')
print(name3[2:-2])
print(name3[3::-1])
print(name3[:5])
