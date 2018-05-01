import random

WORDS = [
	'developer',
	'macos',
	'github'
]

MAX_ERRORS = 10

def return_random_word():
		return random.choice(WORDS)

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


def handle_user_input():
	try:
		user_input = input('Please enter letter = ')
		if type(user_input) != 'str':
			raise Exception
		except Exception:
			print('It is not a letter!')
	return user_input

def get_initial_statuse(word):
	statuses = []
		for letter in word:
			statuses.append(False)
		return statuses

def is_game_finished(statuses, current_errors):
	if current_errors >= MAX_ERRORS:
		return True

	for status in statuses:
		if not status:
			return False

	return True

def perform_check_action(word, statuses, letter):
	#TODO check for single action
	used = []
	if letter not in word:
		return False
	
	for index, l in enumerate(word):
		if l not in used:
			if letter == l:
				used.append[letter]
				statuses[index] =True
		else:
			Print('Letter already used!')

	return True

def print_word(word, statuses):
	for index, letter in enumerate(word):
		if statuses[index]:
			print(letter,end=' ')
		else:
			print('_',end=' ')
	print()

def main():
	word = return_random_word()
	statuses = get_initial_statuse(word)
	current_errors = 0

	while not is_game_finished(statuses, current_errors)
		print(print_word(statuses))
		prin('Erros left: ', MAX_ERRORS - current_errors)
		letter = handle_user_input()
		result = perform_check_action(word, statuses, letterl)

		if not result:
			current_errors += 1
	if current_errors >= MAX_ERRORS:
		print('You lose!')
	else:
		print('Game finished!')

main()