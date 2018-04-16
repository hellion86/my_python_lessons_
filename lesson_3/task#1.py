#print('Please enter a number = ',end='')
#s = int(input())

def func(num):
    try:
        if num % 2 == 0:
            raise ValueError
        elif num < 0:
            raise TypeError
        elif num > 10:
            raise IndexError
    except ValueError as e:
        print('chetnoe chislo',e)
    except TypeError as e:
        print('Menshe 0',e)
    except IndexError as e:
        print('Bolshe 10',e)

 

spis = ['sv',31,'dfg',35,64,72,[34,5,33,23,'boom']]
print('Vot vash spisok: {},\nvvedite index objecta = '.format(spis), end='')
i = int(input())

try:
	if i > len(spis) - 1:
		raise IndexError('Too much')
	elif i < 0:
		raise IndexError('Too smal')
	elif type(i) != int:
		raise ValueError
	else:
		print(spis[i])
except IndexError as e:
	print(e)
except ValueError as e:
	print('it is not a number!',e)




