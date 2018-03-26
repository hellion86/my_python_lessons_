#1 какой язык мы учим: Питон, пайтон, Python, python
#2 какой тип данных у числа 9: int, integer, Int
#3 какой тип данных у числа 4.1: float, флоат
#4 сколько символов в слове строка: 6, шесть
#5 можно ли делать операции с NULL: нет, нельзя, Нет
#6 как в Python обозначается ложь: False
#7 сколько будет сумма 10 и 5: 15, пятьнадцать
#8 как пишется ключевое слово и: and
#9 как в Python обозначается истина: True
#10 как пишется ключеов слово или: or
bonus = 0
answer1 = ['Python','python','питон','пайтон']
answer2 = ['int','integer','целое']
answer3 = ['float', 'флоат']
answer4 = ['6', 'шесть']
answer5 = ['нет', 'нельзя', 'Нет']
answer6 = ['False']
answer7 = ['15, пятьнадцать']
answer8 = ['and']
answer9 = ['True']
answer10 = ['or']


print('Какой язык мы учим? ')
x = input()
for asq in answer1:
    if x == asq:
        bonus = bonus + 1
print('какой тип данных у числа 9? ')
x = input()
for asq in answer2:
    if x == asq:
        bonus = bonus + 1
print('какой тип данных у числа 4.1? ')
x = input()
for asq in answer3:
    if x == asq:
        bonus = bonus + 1
print('сколько символов в слове строка? ')
x = input()
for asq in answer4:
    if x == asq:
        bonus = bonus + 1
print('можно ли делать операции с NULL? ')
x = input()
for asq in answer5:
    if x == asq:
        bonus = bonus + 1
print('как в Python обозначается ложь? ')
x = input()
for asq in answer6:
    if x == asq:
        bonus = bonus + 1
print('сколько будет 5 + 10? ')
x = input()
for asq in answer7:
    if x == asq:
        bonus = bonus + 1
print('как пишется логическое и? ')
x = input()
for asq in answer8:
    if x == asq:
        bonus = bonus + 1
print('как обозначается истина? ')
x = input()
for asq in answer9:
    if x == asq:
        bonus = bonus + 1
print('как пишется логическое или? ')
x = input()
for asq in answer10:
    if x == asq:
        bonus = bonus + 1
        


print('Вы отгадали правильно %s загадок' %bonus)  
