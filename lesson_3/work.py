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

def spisok(s):
	try:
		for i in s: 
			if type(i) == int:
				s = sorted(s)
		return s 
	except ValueError as e:
		print('It is not a list!',e)
		return s

print(spisok((45,3,0,5,7,4,3)))


def listsum(*numList):
    x = 1
    for i in range(len(numList)):
    	x = x * numList[i]
    return x 
   
print(listsum(1,2,3,4,5))

'''def slovar(r):
	for i in r:
	    r[i] = str(r[i])
    return r

print(slovar({s:1,b:2,t:4}))'''
	