lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

map_testing = list(map(lambda x: 'Fruit: ' + x, lst_check))

#print(list(map_testing))

assert 'Fruit: plums' in map_testing
assert 'Fruit: kiwi' in map_testing
