
import random

def quest():
	return int(random.randint(1,100))
 
def answer(num):
	try:
		answer = int(input('Vvedite vashu cifru:'))
		if answer > num:
			print('Moe chislo menshe')
		elif answer < num:
			print('Moe chislo bolshe')
			return 0
		else:
			print('Vi ugadali!, moe chsilo bilo {}'.format(answer))
			return 1
	except Exception:
		print('Vi vveli ne chislo!')
		
def game(num):
	while not answer(num):
		print('*************')

game(quest())
try:
	while input('Play again?: (y/n)').lower() == 'y':
		game(quest())
except Exception:
	print('Bad input')

print('Bye')






