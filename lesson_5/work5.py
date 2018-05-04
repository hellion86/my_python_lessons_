 
'''class Door:
    def open(self):
        print('Self is:', self)
        print('Door is opened')
        self.opened = True

d = Door()
d.open()



class Car:
    pass

c = Car()
c.wheels = 'Pirelli'
c.seat = 'Some seat'
  

print(c.wheels)




class Terminal:
    def hello(self, user_name):
        print('Self is the object itself: ',self)
        print('Hello, ', user_name)

t = Terminal()
t.hello('Slava')
t.hello('Lena')

class Window:
    is_opened = False

    def open(self):
            self.is_opened = not self.is_opened
            print('Windows is now', self.is_opened)

w = Window()
w1 = Window()

print('Initial state', w.is_opened, w1.is_opened)

w.open()
print('New state: ', w.is_opened, w1.is_opened)


class TestClass:
    engine = 'V8 turbo'
    def __init__(self,color):
        self.coror = color
        
t = TestClass('red')

t1 = TestClass('white')

print(t.coror,t1.coror)
 

class Table:
    def __init__(self, number_of_legs):
        print('New table has {}'.format(number_of_legs))


t = Table(4)
t = Table(2)

class Chair:
        def __init__(self, color):
            self.color = color

c = Chair('green')
print(c, c.color)

c1 = Chair('red')
print(c1.color)
print('variable c did not change!', c.color)
 


class Parent(object):
    def __init__(self):
        print('Parent inited')
        self.value = 'Parent'

    def do(self):
        print('Parent do(): {}'.format(self.value))


class Child(Parent):
    def __init__(self):
        print('Child inited')
        self.value = 'Child'

parent = Parent()
parent.do()

child = Child()
child.do()
'''













