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

#for i in range(1,100):
#    if i % 7 == 0:
#        print(i)

'''matrix = [
        [23,5,7],
        [33,54,86],
        [1,23,67],
        [57,56,34]
    ]

for i in matrix:
    print(i)

for s in matrix:
    for j in s:
        print(j)
'''
s = 0

m = [1,2,3,4,5]
for i in range(len(m)):
    print(i,':',m[i])
    s = m[i] + s
    print(s)
    


def listsum(*numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return int(numList[0]) + int(listsum(numList[1:]))

listsum(1,2,3,4,5)