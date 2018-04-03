not_a_list = (1,2)
list1 = [1,2]
list2 = list(not_a_list)

print(list1 == list2 , list1 == not_a_list)

list1.append(3)
print('append() returns None:', list1.append(4))
print(list1)

list1.append(list2)
print(list1)

list1.extend(list2)
print(list1)

list1.insert(1, 'inserted value')
print(list1)

var = ['bar']
new_var = var
var.append('foo')
var[0] = 'baz'
print(new_var)

test_list = ['pop','remove','del']

popped = test_list.pop(0)
print('popped value is "{}"'.format(popped))

test_list.remove('remove')
print(test_list)

del test_list[0]
print(test_list)

multi = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11]
]

for row in multi:
    print(row)
    for element in row:
        print('element: ', element)

print('range', range(1,10))
for i in list(range(1,15,2)):
    print(i)
        
