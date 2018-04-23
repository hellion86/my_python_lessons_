import random

print('Eto igra nazivaetsa "Vicekica", u vas 10 jizney chtobi otgadat` vse slovo, vvodite posimvolno!')
# vvodnie dannie
text = ['mama','kofe','vecher','beznadega','popitka']
lives = 10
quest = list(random.choice(text))
temp = list('-' * len(quest))

def beuaty(list):
	s = ''
	for i in list:
		s = s + i
	return s

print(beuaty(temp))

'''def isexist(symbol):
	em = []
	em.append(symbol)
	for s in em:
		if symbol == s:		
'''

def howmuch(lives):
	if lives == 6:
		print('You already have only 5 chances!')
	elif lives == 3:
		print('Danger, danger, achtung, 3 lives leave!')
	elif lives == 0:
		print('Doigralsya, Game over !')


while lives >= 0:
	lives -= 1
	howmuch(lives)
	if lives == 0:
		break
	if temp == quest:
			print('You win!, my word was ***{}!***'.format(beuaty(quest)))
			break
	bukva = input('Vvedite vashu bukvu: ')
	for i in range(len(quest)):
		if quest[i] == bukva:
			temp.pop(i)
			temp.insert(i,bukva)
	print(beuaty(temp))
		


