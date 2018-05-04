

class trash(object):
	"""docstring for trash"""
	def __init__(self, emkost):
		self.emkost = emkost

	def change_size(self,emkost):
		self.emkost = emkost

	def get_size(self):
		print('Size of basket is = {}'.format(self.emkost))

	def put_in_trash(self,object):
		if object.size < self.emkost:
			print('In a trash {}'.format(object.size))
		else:
			print('It is too big for trash')

class packet(trash):
	def get_size(self):
		print('Size of packet is = {}'.format(self.emkost))

	def put_in_trash(self,object):
		if object.size < self.emkost:
			print('In a packet {}'.format(object.size))
		else:
			print('It is too big for packet')

class items():
	def __init__(self,size):
		self.size = size


trash1 = trash(15)
print(trash1.get_size())
trash1.change_size(222)
print(trash1.get_size())
 
packet1 = packet(35)
print(packet1.get_size())
packet1.change_size(45)
 

item1 = items(34)
print(item1.size)
trash1.put_in_trash(item1)
