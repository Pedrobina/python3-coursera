# Write code using zip and filter so that these lists (l1 and l2) are combined into one big list of pairs and assigned to the variable opposites
# if both elements of the pair are longer than 3 characters. Note: be sure to use list to convert the result into a list.


l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']

opposites = None # Replace "None" with an expression that uses `zip` and `filter`


assert ('left', 'right') in opposites
# omit if either word is shorter than 3 characters...
assert ('up', 'down') not in opposites