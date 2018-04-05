'''
x = int(input("Введите длину: "))
y = int(input("Введите длину: "))

print("Площадь = ", x * y)
'''

'''x
x = int(input("Введите 1 число: "))
y = int(input("Введите 2 число: "))
action = str(input("Введите знак: "))

if action == '+':
    print("Сумма = ", x + y)
else:
    print("Разница = ", x - y)
'''
'''
def isProst(x):
    if x==1:
        return True
    for i in range(2,x-1):
        if not x%i:
            return False
    return True
i = 2
x = int(input("Введите 1 число: "))

while i <= x:
    i = i + 1
    if isProst(i):
        print(i)
 '''
x = int(input("Введите 1 число: "))
y = int(input("Введите 2 число: "))
for i in range(x,y):
    if i%5 == 0:
        print (i)

