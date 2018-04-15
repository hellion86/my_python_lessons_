'''try:
	1 / 0
except:
	print('Ошибко')

try:
	1 / 1
except:
	print('Ошибко')
'''
'''
try:
        1 / 0
        
except:
        print('Error is here', 1 / 0)
'''
'''try:
        print(1 / 0)
except:
        print('0!!')

try:
        print(1 / 0)
except Exception:
        print('0!!')
'''

def obrabotka(x):
	try:
		1 / x
	except ZeroDivisionError as e:
		print('atatata',e)
	except TypeError as e: 
		print('Wrong type!',e)
	except ValueError as e:
		print('***********************',e)
	return 1 / x

#obrabotka(int('d'))
import random

def obarbota1():
	execption = random.choice([ZeroDivisionError,TypeError,RuntimeError])
	try:
		 raise execption
	except ZeroDivisionError:
		print("Delenie na nol`")
	except TypeError:
		print("Neverniy tip dannih")
	except RuntimeError:
		print("Ya vas ne ponimat`")

print(obarbota1())

def spisok(s):
	mm = list()
	for i in s: 
		if isinstance(i,int):
			mm.append(i)
		else:
			raise ValueError('It is not a list!')
	return sorted(mm)

print(spisok((45,3,0,5,7,4,3)))

#дедовский способ перемножить элеметны списка
'''def listsum(*numList):
    x = 1
    for i in range(len(numList)):
    	x = x * numList[i]
    	print(x,numList[i])
    return x 
   
print(listsum(1,2,3,4,5))'''
#новый способ
from functools import reduce 

lst = [1,2,3,4]

print(reduce(lambda res, x : x * res, lst))

def slovar(r):
	ss = dict()
	for i,key in r.items():
		ss[str(key)] = key
	return ss

print(slovar({'s':436,'b':6547,'t':4564}))

slovar1 = {'s1':436,'s2':6547,'s3':4564}
for x,y in slovar1.items():
	print(x,y)