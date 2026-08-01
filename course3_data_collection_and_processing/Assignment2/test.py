list_a = [1, 2, 3]
list_b = [10, 20, 30]

# Sum elements from both lists side by side
summed = map(lambda x, y: x + y, list_a, list_b)

print(list(summed)) 