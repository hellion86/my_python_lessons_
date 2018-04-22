
import random

quest = int(random.randint(1,100))
 

print('Ya zagadal chislo, poproby`te otgadat`!')
print()
num = 0 
while True:
	try:
		answer = int(input('Vvedite vashu cifru:'))
		if answer > quest:
			print('Moe chislo menshe')
			num += 1
		elif answer < quest:
			print('Moe chislo bolshe')
			num += 1
		else:
			print('Vi ugadali!, moe chsilo bilo {}, vi ego otgadali za {} popitok'.format(quest,num))
			break
	except TypeError:
		print('Vi vveli ne chislo!')
		num +=1
	except ValueError:
		print('Vi vveli ne chislo!')
		num +=1