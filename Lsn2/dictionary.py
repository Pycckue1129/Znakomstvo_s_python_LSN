# d = {}
# d = dict()
#
# d['q'] = 'qwerty'
# print(d)
#
# d['w'] = 'werty'
# print(d)
# print(d['q'])

dictionary = {}
dictionary = {'up': 'u', 'left': 'l', 'down': 'd', 'right': 'r'}
dictionary[895] = 98879
print(dictionary['up'])
print(dictionary[895])
del dictionary[895]  # Удаление элемента
for item in dictionary:
    print('{}: {}'.format(item, dictionary[item]))
for (k, v) in dictionary.items():
    print(k, v)
