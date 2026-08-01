#Create a new list called thirds by iterating through the contents of list__of_lists, collecting the third element of each sublist.

list__of_lists = [
    ['purple', 'mauve', 'blue'],
    ['red', 'maroon', 'blood orange', 'crimson'],
    ['sea green', 'cornflower', 'lavender', 'indigo'],
    ['yellow', 'amarillo', 'mac n cheese', 'golden rod']
]
thirds = []
for lst in list__of_lists:
    thirds.append(lst[2])


assert thirds == ['blue', 'blood orange', 'lavender', 'mac n cheese']