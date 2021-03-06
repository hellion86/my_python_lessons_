#task 1
class Person():
	def __init__(self, age, name):
		self.age = age
		self.name = name
		self.notes = []

	def know(self,name):
		if not name in self.notes:
			self.notes.append(name)
		else:
			print('You are already meet early with {}'.format(name.name))
		#self.know = name
		#print('Nice to meet you, {}'.format(self.know))

	def is_know(self, name):
		 if name in self.notes:
		 	print('You know {}'.format(name.name))
		 else:
		 	print('You dont know {}'.format(name.name))

per1 = Person(32, 'Slava')
per2 = Person(34, 'Elena')
per3 = Person(34, 'Pavel')

per1.know(per2)
per1.know(per2)
per1.is_know(per3)

#task 2

class Printer():
	def __init__(self):
		 pass
	def log(self,*values):
		print(",".join(values))

class Format(Printer):
	def formatted_log(self,*values):
		print('***************')
		self.log(*values)
		print('***************')
		

pr1 = Format()
pr1.log('adsdfsdf','sdfsdf')
pr1.formatted_log('adsdfsdfsdfsdfsdf','sdfsdf')

#task 3

class Animal():
	def __init__(self, name, danger):
		self.name = name
		#self.type = anim_type
		self.danger = danger
	
	def description(self):
		if self.danger:
			print('It is {}, very danger for Human'.format(self.name))
		else:
			print('It is {}, not danger for Human'.format(self.name))



class Human():
	def __init__(self, name):
		self.name = name

	def is_danger(self, animal):
		if animal.danger == True:
			print('It is {}, very danger for {}'.format(animal.name,self.name))
		else:
			print('It is {}, not danger for {}'.format(animal.name,self.name))


animal1 = Animal('leopard',True)
animal2 = Animal('Tiger', True)
animal3 = Animal('Turtle', False)

animal1.description()
animal3.description()

human1 = Human('Oleg')
human1.is_danger(animal1)
human1.is_danger(animal3)