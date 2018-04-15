#l = [1,5,2,7,55,34,32,8]

#print(sorted(l))

#s = { 1:'1', 2:'2', 3:'3', 4:'4', 5:'5' }

#for i in s:
#    print(i,s[i])

'''m = (23.4,23.45,12.67,87.9,34.33,57.1,45.89)
print(m)
kk = sorted(m)
print(kk[0],kk[len(kk)-1])'''

#l = ['Earth','Russia','Moscow']

#l[0]
##for i in l:
#print(l[0]+'->'+l[1]+'->'+l[2])

#test = '/bin:/usr/bin:/usr/local/bin'
#m = test.split(":")
#print(m)

'''for i in range(1,100):
    if i % 7 == 0:
        print("Это гуд = ", i)
    else:
    	print("Это совсем не гуд = ", i)
'''
'''
import random

row = 4
table = 3
matrix = []

for r in range(row):
	matrix.append([])
	for t in range(table):
		matrix[r].append(random.randint(0, 10))

print('Vsya matrica', matrix)
print()

print('Stroki')
for r in range(row):
	for t in range(table):
		print(matrix[r][t], end='_')
	print()
print()

print('Stolbci')
for t in range(table):
	for r in range(row):
		print(matrix[r][t], end='_')
	print()

    '''


'''m = [23.4,23.45,12.67,87.9,34.33,57.1,45.89]
for i in range(len(m)):
    print(i,':',m[i])
'''

'''l = ['dfg','to-delete','sdf','4rf','to-delete','erfd','to-delete'] 

for i in l:
	if i == 'to-delete':
		l.pop(l.index(i))

print(l)'''

'''for i in range(10,0,-1):
	print(i)
'''
from functools import reduce

seq = [1,2,5,6,4,6,]


s = reduce(lambda res, x: res*x, seq)

print(s)

#for s,item in enumerate(seq):
#	ss = item * seq[s]
#	print(item ,':' ,s)
