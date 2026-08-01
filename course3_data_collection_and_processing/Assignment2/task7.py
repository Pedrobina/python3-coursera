#Below, we have provided a species list and a population list. Use zip to combine these lists into one list of tuples called pop_info.
# From this list, create a new list called endangered that contains the names of species whose populations are below 2500.


species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]

pop_info = None   # Replace "None" with an expression that makes pop_info a list of tuples (each first item is a species string and each second item is a number, for that species' population)
endangered = None # Replace "None" with an expression that makes `endangered` a list of strings (species whose population is below 2500)



assert ('golden retriever', 10000) in pop_info
assert 'golden retriever' not in endangered
assert 'black rhino' in endangered