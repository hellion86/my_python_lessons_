'''def chisla(a,b):
	if a > 0 and b > 0:
		c = a + b
	elif a < 0 and b < 0:
		c = abs(a - b)
	elif a * b < 0: 
		c = 0
	else:
		print('Net sovpadeniy')
	return c

print(chisla(1,3))
print(chisla(-1,-5))
print(chisla(-10,3))

def minmax(a,b,c):
	#l = min(a,b,c)
	#print('min',l)
	if a <= b and a <= c:
		print(b,c)
	elif c <= a and c <= b:
		print(b,a)
	elif b <= a and b <= c:
		print(a,c)

minmax(1,3,7)
minmax(3,33,27)
minmax(13,3,17)

ddef clever(spis,flag):
	l = []
	for i in spis:
		if flag:
			if i % 2 == 0:
				l.append(i)
		else:
			if i % 2 != 0:
				l.append(i)
	return l

my = [1,5,6,7,8,9,5,5,4,0]

print(clever(my,True))'''

def minmax(*args):
	for i in args:
		s = min(args)
		b = max(args)
	return s,b

print(minmax(1,3,4,5,32,5,7,7,34,633,0.1))

def stroka(str, case=True):
	if case:
		newstr = str.upper()
	else:
		newstr = str.lower()
	return newstr

print(stroka('PrIvEt',False))


def slipper(*str, g=':'):
    l = ''
    
    for i in str:
        if len(i) >= 3:
            l = l + i + g
    return l

print(slipper('123','456','vhngf','ghn','h','h','m','j','BOOM'))

def strings_concat(*args, glue=':'):
	out_string = '';
	idx = 0;
	for item in args :
		if len(item) > 2 :
			out_string += (glue + item) if idx else item;
			idx += 1;
		
	return out_string;	

print(strings_concat('as', ',rf,,ert','ert4','adsadsdad', 'asdasdsda')); 